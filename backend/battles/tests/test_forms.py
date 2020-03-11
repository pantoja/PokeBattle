from django.test import TestCase

from model_mommy import mommy

from battles.forms import CreateTeamForm


class TestCreateTeamForm(TestCase):
    def setUp(self):
        self.trainer = mommy.make("users.User")
        self.pokemon_1 = mommy.make("pokemon.Pokemon")
        self.pokemon_2 = mommy.make("pokemon.Pokemon")
        self.pokemon_3 = mommy.make("pokemon.Pokemon")
        self.battle = mommy.make("battles.Battle")

    def test_create_a_team(self):
        params = {
            "initial": {"trainer": self.trainer},
            "data": {
                "pokemon_1": self.pokemon_1,
                "pokemon_2": self.pokemon_2,
                "pokemon_3": self.pokemon_3,
            },
        }
        form = CreateTeamForm(**params)
        self.assertTrue(form)

    def test_pokemon_exceeds_points_limit(self):
        params = {
            "initial": {"trainer": self.trainer, "battle": self.battle},
            "data": {
                "pokemon_1": mommy.make("pokemon.Pokemon", id=1).id,
                "pokemon_2": mommy.make("pokemon.Pokemon", id=2).id,
                "pokemon_3": mommy.make("pokemon.Pokemon", id=3).id,
            },
        }
        form = CreateTeamForm(**params)
        self.assertTrue(form.is_valid())
