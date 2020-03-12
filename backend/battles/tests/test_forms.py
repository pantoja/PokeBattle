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
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": mommy.make("pokemon.Pokemon", id=1).id,
                "pokemon_2": mommy.make("pokemon.Pokemon", id=2).id,
                "pokemon_3": mommy.make("pokemon.Pokemon", id=3).id,
            },
        }
        form = CreateTeamForm(**params)
        self.assertTrue(form.is_valid())

    def test_team_cant_have_identical_pokemon(self):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": mommy.make("pokemon.Pokemon", id=1).id,
                "pokemon_2": mommy.make("pokemon.Pokemon", id=1).id,
                "pokemon_3": mommy.make("pokemon.Pokemon", id=2).id,
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())

    def test_team_cant_have_invalid_pokemon(self):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": mommy.make("pokemon.Pokemon", id=-5).id,
                "pokemon_2": mommy.make("pokemon.Pokemon", id=1).id,
                "pokemon_3": mommy.make("pokemon.Pokemon", id=2).id,
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())

    def test_pokemon_exceeds_points_limit(self):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": mommy.make("pokemon.Pokemon", id=493).id,
                "pokemon_2": mommy.make("pokemon.Pokemon", id=2).id,
                "pokemon_3": mommy.make("pokemon.Pokemon", id=3).id,
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())
