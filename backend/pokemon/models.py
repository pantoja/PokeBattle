from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    sprite = models.URLField()

    attack = models.IntegerField("Attack")
    defense = models.IntegerField("Defense")
    hp = models.IntegerField("HP")

    def __str__(self):
        return self.name
