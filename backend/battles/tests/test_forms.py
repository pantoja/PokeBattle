from django.test import TestCase

from model_mommy import mommy

from battles.forms import CreateBattleForm


class TestCreateBattleForm(TestCase):
    def setUp(self):
        self.creator = mommy.make("users.User")
        self.opponent = mommy.make("users.User")

    def test_form_is_valid(self):
        params = {
            "initial": {"user_creator": self.creator},
            "data": {"user_opponent": self.opponent},
        }
        form = CreateBattleForm(**params)
        self.assertTrue(form)
