from django.test import TestCase

import mock
from model_mommy import mommy

from battles.forms import CreateBattleForm, CreateTeamForm


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

    @mock.patch("battles.helpers.get_pokemon_stats")
    def test_pokemon_exceeds_points_limit(self, mock_get_pokemon_stats):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": mommy.make("pokemon.Pokemon", id=493).id,
                "pokemon_2": mommy.make("pokemon.Pokemon", id=2).id,
                "pokemon_3": mommy.make("pokemon.Pokemon", id=3).id,
            },
        }
        mock_get_pokemon_stats.return_value = {
            "name": "mock_name",
            "id": 1,
            "sprite": "",
            "attack": 360,
            "defense": 360,
            "hp": 360,
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())
        assert mock_get_pokemon_stats.called


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
