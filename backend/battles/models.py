from django.db import models

from users.models import User


class Battle(models.Model):
    user_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Creator", related_name="user_creator"
    )
    user_opponent = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Opponent", related_name="user_opponent"
    )

    def __str__(self):
        return "Battle nº " + str(self.id)


class Team(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name="battle")
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Trainer", related_name="trainer"
    )
