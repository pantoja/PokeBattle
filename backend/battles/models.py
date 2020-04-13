from django.core.exceptions import ValidationError
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
    settled = models.BooleanField(default=False)
    winner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Winner",
        related_name="winner",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-pk"]

    def clean(self):
        if self.user_creator == self.user_opponent:
            raise ValidationError("The creator and opponent users can't be the same")
        if self.settled is True and self.winner is None:
            raise ValidationError("Settled battles should have a defined winner")
        if self.settled is False and self.winner:
            raise ValidationError("Battles with defined winner should be marked as settled")

    def __str__(self):
        return "Battle nº " + str(self.id)


class Team(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name="teams")
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Trainer", related_name="teams"
    )
    first_pokemon = models.ForeignKey(
        Pokemon, related_name="first_pokemon", on_delete=models.CASCADE
    )
    second_pokemon = models.ForeignKey(
        Pokemon, related_name="second_pokemon", on_delete=models.CASCADE
    )
    third_pokemon = models.ForeignKey(
        Pokemon, related_name="third_pokemon", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-battle"]

    def __str__(self):
        return f"{self.trainer}'s team"
