from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy

from battles.models import Battle


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
