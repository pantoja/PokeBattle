from django.db import models

from pokemon.models import Pokemon
from users.models import User


class Battle(models.Model):
    user_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Creator", related_name="created_battle"
    )
    user_opponent = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Opponent", related_name="invited_to_battle"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Battle nº " + str(self.id)


class Team(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name="teams")
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Trainer", related_name="teams"
    )
    team = models.ManyToManyField(Pokemon, verbose_name="Team")

    def __str__(self):
        return f"{self.trainer}'s team"
