from django.test import Client
from django.urls import reverse

from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from api.battles.serializers import CreateBattleSerializer, DetailBattleSerializer


class TestListBattlesView(APITestCase):
    def setUp(self):
        self.settled_url = reverse("api:battle:list_settled")
        self.active_url = reverse("api:battle:list_active")
        self.user = mommy.make("users.User")
        self.client = Client()
        self.client.force_login(self.user)
        self.battle_set = [
            mommy.make("battles.Battle", user_creator=self.user, settled=True),
            mommy.make("battles.Battle", user_opponent=self.user, settled=True),
            mommy.make("battles.Battle", user_opponent=self.user, settled=True),
            mommy.make("battles.Battle", user_creator=self.user, settled=False),
            mommy.make("battles.Battle", user_opponent=self.user, settled=False),
            mommy.make("battles.Battle", settled=True),
            mommy.make("battles.Battle", settled=False),
        ]

    def test_list_active_battles(self):
        response = self.client.get(self.settled_url)
        data = [battle["id"] for battle in response.json()]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 3)

    def test_list_settled_battles(self):
        response = self.client.get(self.active_url)
        data = [battle["id"] for battle in response.json()]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)

    def test_unauthenticated_raises_error(self):
        self.client.logout()
        response = self.client.get(self.active_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestDetailBattleView(APITestCase):
    def setUp(self):
        self.user = mommy.make("users.User")
        self.user_2 = mommy.make("users.User")
        self.client = Client()
        self.client.force_login(self.user)
        self.battle = mommy.make(
            "battles.Battle", user_creator=self.user, user_opponent=self.user_2
        )
        self.team = mommy.make("battles.Team", battle=self.battle, trainer=self.user)
        self.url = "/api/battle/1"

    def test_detail_battle(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        battle = DetailBattleSerializer(self.battle)
        self.assertEqual(battle.data, response.data)

    def test_unlogged_cant_see_battle(self):
        self.client.logout()
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_opponent_cant_see_unsettled_battle(self):
        self.client.force_login(self.user_2)
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_not_in_battle_cant_see_battle(self):
        self.client.force_login(mommy.make("users.User"))
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestCreateBattleView(APITestCase):
    def setUp(self):
        self.user = mommy.make("users.User")
        self.client = Client()
        self.client.force_login(self.user)
        self.url = reverse("api:battle:create_battle")

    def test_create_battle(self):
        battle = mommy.make("battles.Battle", user_creator=self.user)
        battle = CreateBattleSerializer(battle)
        response = self.client.post(self.url, battle.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unlogged_cant_create_battle(self):
        self.client.logout()
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_user_not_creator_of_battle(self):
        battle = mommy.make("battles.Battle")
        battle = CreateBattleSerializer(battle)
        response = self.client.post(self.url, battle.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestCreateTeamView(APITestCase):
    def setUp(self):
        self.user = mommy.make("users.User")
        self.client = Client()
        self.client.force_login(self.user)
        self.url = reverse("api:battle:create_team")
        self.pokemon_set = mommy.make("pokemon.Pokemon", attack=50, defense=50, hp=50, _quantity=3)

    # TODO: Create team test

    def test_unlogged_cant_create_battle(self):
        self.client.logout()
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
