from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from model_mommy import mommy

from battles.models import Battle, Team


class TestTeamModel(TestCase):
    def setUp(self):
        self.battle = mommy.make("battles.Battle")
        self.trainer = mommy.make("users.User")
        self.trainer_opponent = mommy.make("users.User")
        self.pokemon_1 = mommy.make("pokemon.Pokemon", id=1)
        self.pokemon_2 = mommy.make("pokemon.Pokemon", id=2)
        self.pokemon_3 = mommy.make("pokemon.Pokemon", id=3)
        self.team = (self.pokemon_1.id, self.pokemon_2.id, self.pokemon_3.id)

    def test_create_team(self):
        item = Team.objects.create(
            trainer=self.trainer,
            battle=self.battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )
        check = Team.objects.filter(id=item.id).exists()
        self.assertTrue(check)

    def test_create_active_battle(self):
        battle = Battle.objects.create(
            user_creator=self.trainer, user_opponent=self.trainer_opponent
        )
        self.assertTrue(battle)

    def test_create_settled_battle(self):
        battle = Battle.objects.create(
            user_creator=self.trainer,
            user_opponent=self.trainer_opponent,
            settled=True,
            winner=self.trainer,
        )
        self.assertTrue(battle)

    def test_battle_cant_be_settled_without_winner(self):
        battle = Battle.objects.create(
            user_creator=self.trainer, user_opponent=self.trainer_opponent, settled=True
        )
        self.assertRaises(ValidationError, battle.clean)

    def test_battle_cant_have_winner_without_being_settled(self):
        battle = Battle.objects.create(
            user_creator=self.trainer,
            user_opponent=self.trainer_opponent,
            winner=self.trainer_opponent,
        )
        self.assertRaises(ValidationError, battle.clean)


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
