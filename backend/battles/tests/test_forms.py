from django.test import TestCase

from model_mommy import mommy

from battles.forms import CreateBattleForm, CreateTeamForm


class TestCreateTeamForm(TestCase):
    def setUp(self):
        self.trainer = mommy.make("users.User")
        self.pokemon_1 = mommy.make("pokemon.Pokemon", id=1)
        self.pokemon_2 = mommy.make("pokemon.Pokemon", id=2)
        self.pokemon_3 = mommy.make("pokemon.Pokemon", id=3)
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
            "initial": {"trainer": self.trainer},
            "data": {
                "pokemon_1": mommy.make(
                    "pokemon.Pokemon", id=1, attack=200, defense=200, hp=200
                ).id,
                "pokemon_2": mommy.make(
                    "pokemon.Pokemon", id=2, attack=200, defense=200, hp=200
                ).id,
                "pokemon_3": mommy.make(
                    "pokemon.Pokemon", id=3, attack=200, defense=200, hp=200
                ).id,
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())

    def test_send_result_email(self):
        params = {
            "initial": {"battle": self.battle},
            "data": {
                "trainer": self.trainer,
                "pokemon_1": self.pokemon_1.id,
                "pokemon_2": self.pokemon_2.id,
                "pokemon_3": self.pokemon_3.id,
            },
        }
        CreateTeamForm(**params)

        self.second_trainer = mommy.make("users.User")
        params = {
            "initial": {"battle": self.battle},
            "data": {
                "trainer": self.second_trainer,
                "pokemon_1": self.pokemon_1.id,
                "pokemon_2": self.pokemon_2.id,
                "pokemon_3": self.pokemon_3.id,
            },
        }


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
