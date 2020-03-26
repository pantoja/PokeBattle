from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy

from battles.models import Battle, Team


class TestCreateBattleView(TestCase):
    view_name = "battles:create_battle"

    def setUp(self):
        self.creator = mommy.make("users.User")
        self.creator.save()
        self.opponent = mommy.make("users.User")
        self.view_url = reverse(self.view_name)
        self.client = Client()
        self.client.force_login(self.creator)

    def test_create_battle(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        response = self.client.post(self.view_url, post_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_created_battle_user_is_the_same_as_the_logged_one(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        self.client.post(self.view_url, post_data, follow=True)

        creator = Battle.objects.last().user_creator
        opponent = Battle.objects.last().user_opponent
        self.assertEqual((creator, opponent), (self.creator, self.opponent))

    def test_unlogged_user_cant_create_battle(self):
        with self.assertRaises(TypeError):
            post_data = {"user_creator": None, "user_opponent": self.opponent.id}
            self.client.post(self.view_url, post_data, follow=True)

    def test_create_battle_redirects_to_success_url(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        response = self.client.post(self.view_url, post_data, follow=True)
        self.assertRedirects(
            response,
            "/create-team/1",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )


class TestDetailBattleView(TestCase):
    view_name = "battles:detail_battle"

    def setUp(self):
        self.trainer_1 = mommy.make("users.User")
        self.trainer_2 = mommy.make("users.User")
        self.client = Client()
        self.client.force_login(self.trainer_1)
        self.team = mommy.make("pokemon.Pokemon", _quantity=3)
        self.view_url = reverse(self.view_name, kwargs={"pk": 1})

    def test_detail_battle_successfully(self):
        battle = Battle.objects.create(
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=True,
            winner=self.trainer_1,
        )

        team_1 = Team.objects.create(trainer=self.trainer_1, battle=battle)
        team_1.team.set(self.team)

        team_2 = Team.objects.create(trainer=self.trainer_2, battle=battle)
        team_2.team.set(self.team)
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_user_not_creator_of_active_battle_is_denied(self):
        battle = Battle.objects.create(
            user_creator=self.trainer_2, user_opponent=self.trainer_1, settled=False,
        )

        creator_team = Team.objects.create(trainer=self.trainer_2, battle=battle)
        creator_team.team.set(self.team)

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)

    def test_user_not_in_this_battle_is_denied(self):
        trainer_3 = mommy.make("users.User")

        battle = Battle.objects.create(
            user_creator=self.trainer_2,
            user_opponent=trainer_3,
            settled=True,
            winner=self.trainer_2,
        )

        creator_team = Team.objects.create(trainer=self.trainer_2, battle=battle)
        creator_team.team.set(self.team)

        opponent_team = Team.objects.create(trainer=trainer_3, battle=battle)
        opponent_team.team.set(self.team)

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)

    def test_allow_user_is_creator_of_active_battle(self):
        battle = Battle.objects.create(
            user_creator=self.trainer_1, user_opponent=self.trainer_2, settled=False,
        )

        creator_team = Team.objects.create(trainer=self.trainer_1, battle=battle)
        creator_team.team.set(self.team)

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)
