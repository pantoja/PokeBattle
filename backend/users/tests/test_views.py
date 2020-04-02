from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy


class TestSignUpView(TestCase):
    view_name = "users:signup"

    def setUp(self):
        self.client = Client()
        self.user = mommy.make("users.User")
        self.view_url = reverse(self.view_name)

    def test_logged_user_cant_signup(self):
        self.client.force_login(self.user)
        response = self.client.get(self.view_url)
        self.assertTrue(response.context["user"].is_authenticated)

    def test_successfull_signup(self):
        post_data = {
            "email": self.user.email,
            "password1": self.user.password,
            "password2": self.user.password,
        }
        response = self.client.post(self.view_url, post_data, follow=True)
        self.assertEqual(response.status_code, 200)


class TestLoginView(TestCase):
    view_name = "users:login"

    def setUp(self):
        self.client = Client()
        self.user = mommy.make("users.User")
        self.view_url = reverse(self.view_name)

    def test_logged_user_cant_login(self):
        self.client.force_login(self.user)
        response = self.client.get(self.view_url)
        self.assertTrue(response.context["user"].is_authenticated)
