from django.db import models

from users.models import User


class Battle(models.Model):
    user_opponent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Opponent",)

    def __str__(self):
        return "Battle nº " + str(self.id)
