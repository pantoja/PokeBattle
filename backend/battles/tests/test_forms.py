from django.test import TestCase

import mock
from model_mommy import mommy

from battles.forms import CreateBattleForm, CreateTeamForm
from pokemon.helpers import save_pokemon
from pokemon.models import Pokemon


class TestCreateTeamForm(TestCase):
    def setUp(self):
        self.trainer = mommy.make("users.User")
        self.pokemon_1 = mommy.make("pokemon.Pokemon", attack=50, defense=50, hp=50)
        self.pokemon_2 = mommy.make("pokemon.Pokemon", attack=50, defense=50, hp=50)
        self.pokemon_3 = mommy.make("pokemon.Pokemon", attack=50, defense=50, hp=50)
        self.battle = mommy.make("battles.Battle")

    def test_create_a_team(self):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": self.pokemon_1.id,
                "pokemon_2": self.pokemon_2.id,
                "pokemon_3": self.pokemon_3.id,
                "order_1": "1",
                "order_2": "2",
                "order_3": "3",
            },
        }
        form = CreateTeamForm(**params)
        self.assertTrue(form.is_valid())

    def test_team_cant_have_identical_pokemon(self):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": self.pokemon_1.id,
                "pokemon_2": self.pokemon_1.id,
                "pokemon_3": self.pokemon_3.id,
                "order_1": "1",
                "order_2": "2",
                "order_3": "3",
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            ["Your team has duplicates, please use unique pokemon"], form.non_field_errors()
        )

    @mock.patch("pokemon.helpers.get_pokemon_stats")
    def test_pokemon_exceeds_points_limit(self, mock_get_pokemon_stats):
        mock_get_pokemon_stats.return_value = {
            "name": "mock_name",
            "id": 493,
            "sprite": "",
            "attack": 360,
            "defense": 360,
            "hp": 360,
        }

        save_pokemon(493)
        pokemon_493 = Pokemon.objects.get(id=493)

        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": self.pokemon_1.id,
                "pokemon_2": pokemon_493.id,
                "pokemon_3": self.pokemon_3.id,
                "order_1": "1",
                "order_2": "2",
                "order_3": "3",
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            ["Your team exceeds the 600 points limit, please choose another team"],
            form.non_field_errors(),
        )
        assert mock_get_pokemon_stats.called

    def test_more_than_one_pokemon_cant_battle_in_the_same_round(self):
        params = {
            "data": {
                "trainer": self.trainer.id,
                "pokemon_1": self.pokemon_1.id,
                "pokemon_2": self.pokemon_2.id,
                "pokemon_3": self.pokemon_3.id,
                "order_1": "2",
                "order_2": "2",
                "order_3": "3",
            },
        }
        form = CreateTeamForm(**params)
        self.assertFalse(form.is_valid())
        self.assertEqual(["Please allocate one pokemon per round"], form.non_field_errors())


class TestCreateBattleForm(TestCase):
    def setUp(self):
        self.creator = mommy.make("users.User")
        self.opponent = mommy.make("users.User")

    def test_form_is_valid(self):
        params = {
            "initial": {"user_creator": self.creator},
            "data": {"user_creator": self.creator.id, "user_opponent": self.opponent.id},
        }
        form = CreateBattleForm(**params)
        self.assertTrue(form.is_valid())
