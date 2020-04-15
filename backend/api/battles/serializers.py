from rest_framework import serializers

from battles.models import Battle


class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ["id", "settled", "winner", "user_creator", "user_opponent"]
