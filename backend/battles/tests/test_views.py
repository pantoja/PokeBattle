from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy

from battles.models import Battle


class TestBattleView(TestCase):
    view_name = "battles:create_battle"

    def setUp(self):
        self.creator = mommy.make("users.User")
        self.creator.set_password("1234567s8")
        self.creator.save()
        self.opponent = mommy.make("users.User")
        self.view_url = reverse(self.view_name)
        self.client = Client()
        self.client.login(email=self.creator.email, password="1234567s8")

    def test_create_battle(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        response = self.client.post(self.view_url, post_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_created_battle_user_is_the_same_as_the_logged_one(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        self.client.post(self.view_url, post_data, follow=True)

        creator = Battle.objects.last().user_creator
        opponent = Battle.objects.last().user_opponent
        self.assertTupleEqual((creator, opponent), (self.creator, self.opponent))

    def test_unlogged_user_cant_create_battle(self):
        pass

    def test_create_battle_redirects_to_success_url(self):
        pass
