from django.test import TestCase

from model_mommy import mommy

from battles.models import Team  # noqa
from pokemon.models import Pokemon  # noqa


class TestTeamModel(TestCase):
    def setUp(self):
        self.battle = mommy.make("battles.Battle")
        self.trainer = mommy.make("users.User")
        self.pokemon_set = mommy.prepare("pokemon.Pokemon", _quantity=3)
