from django.test import Client
from django.urls import reverse

from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


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
