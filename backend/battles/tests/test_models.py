from django.test import TestCase

from model_mommy import mommy

from battles.models import Team


class TestTeamModel(TestCase):
    def setUp(self):
        self.battle = mommy.make("battles.Battle")
        self.trainer = mommy.make("users.User")
        self.pokemon_set = mommy.prepare("pokemon.Pokemon", _quantity=3, make_m2m=True)

    def test_create_team(self):
        item = Team.objects.create(trainer=self.trainer, battle=self.battle)
        pkn_id = []
        for pokemon in self.pokemon_set:
            pkn_id.append(pokemon.id)
        item.team.set(pkn_id)
        check = Team.objects.filter(id=item.id).exists()
        self.assertTrue(check)
