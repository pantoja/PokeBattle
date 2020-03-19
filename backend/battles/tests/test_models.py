from django.db.utils import IntegrityError
from django.test import TestCase

from model_mommy import mommy

from battles.models import Battle


class TestTeamModel(TestCase):
    def setUp(self):
        self.battle = mommy.make("battles.Battle")
        self.trainer = mommy.make("users.User")
        self.pokemon_set = mommy.prepare("pokemon.Pokemon", _quantity=3)


class TestBattleModel(TestCase):
    def setUp(self):
        self.creator = mommy.make("users.User")
        self.opponent = mommy.make("users.User")

    def test_create_battle(self):
        item = Battle.objects.create(user_creator=self.creator, user_opponent=self.opponent)
        check = Battle.objects.filter(id=item.id).exists()
        self.assertTrue(check)

    def test_create_empty_field_battle(self):
        with self.assertRaises(IntegrityError):
            Battle.objects.create(user_creator=self.creator, user_opponent=None)
