from django.core import mail
from django.test import TestCase

from model_mommy import mommy

from battles.models import Battle
from battles.tasks import run_battle_task


class TestBattleTasks(TestCase):
    def setUp(self):
        self.battle = mommy.make("battles.Battle")
        self.team_1 = mommy.make(
            "battles.Team", trainer=self.battle.user_creator, battle=self.battle
        )
        self.team_2 = mommy.make(
            "battles.Team", trainer=self.battle.user_opponent, battle=self.battle
        )
        self.url = "test.url"

    def test_change_battle_status(self):
        run_battle_task(self.battle.pk, self.url)
        battle = Battle.objects.get(pk=self.battle.pk)
        self.assertTrue(battle.settled)
        self.assertTrue(battle.winner)

    def test_send_result_email(self):
        run_battle_task(self.battle.pk, self.url)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "PokeBattle - Here's the result of your battle")
