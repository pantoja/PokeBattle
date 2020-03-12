from django.test import TestCase

from model_mommy import mommy

from battles.models import Team


class TestTeamModel(TestCase):
    def setUp(self):
        self.battle = mommy.make("battles.Battle")
        self.trainer = mommy.make("users.User")
        self.pokemon_1 = mommy.make("pokemon.Pokemon", id=1)
        self.pokemon_2 = mommy.make("pokemon.Pokemon", id=2)
        self.pokemon_3 = mommy.make("pokemon.Pokemon", id=3)
        self.team = (self.pokemon_1.id, self.pokemon_2.id, self.pokemon_3.id)

    def test_create_team(self):
        item = Team.objects.create(trainer=self.trainer, battle=self.battle)
        item.team.set(self.team)
        check = Team.objects.filter(id=item.id).exists()
        self.assertTrue(check)
