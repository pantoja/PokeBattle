from django.test import TestCase

from model_mommy import mommy

from users.forms import InviteFriendForm, UserSignUpForm


class TestSignUpForm(TestCase):
    def setUp(self):
        self.user = mommy.make("users.User")

    def test_signup_successfully(self):
        params = {
            "data": {
                "email": "new_user@account.com",
                "password1": "pass1257",
                "password2": "pass1257",
            },
        }

        form = UserSignUpForm(**params)
        self.assertTrue(form.is_valid())

    def test_cannot_create_account_with_existing_email(self):
        params = {
            "data": {
                "email": self.user.email,
                "password1": self.user.password,
                "password2": self.user.password,
            },
        }

        form = UserSignUpForm(**params)
        self.assertFalse(form.is_valid())
        self.assertIn("User with this Email already exists.", form["email"].errors)


class TestInviteFriendForm(TestCase):
    def setUp(self):
        self.user = mommy.make("users.User")

    def test_invite_user_succesfully(self):
        params = {
            "data": {"email": "new_user@email.com"},
        }
        form = InviteFriendForm(**params)
        self.assertTrue(form.is_valid())

    def test_invite_already_signed_user(self):
        params = {"data": {"email": self.user.email}}
        form = InviteFriendForm(**params)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            ["This user already has an account"], form.non_field_errors(),
        )
