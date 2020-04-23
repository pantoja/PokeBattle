from django.db import models
from django.db.models import Q


class BattleManager(models.Manager):
    def filter_by_status(self, user, status):
        return self.filter(Q(user_creator=user) | Q(user_opponent=user), settled=status)
