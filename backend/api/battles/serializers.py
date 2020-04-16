from rest_framework import serializers

from battles.helpers.common import duplicate_in_set, pokemon_team_exceeds_limit
from battles.models import Battle, Team


class ListBattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ["id", "settled", "winner", "user_creator", "user_opponent"]


class BattleTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["trainer", "first_pokemon", "second_pokemon", "third_pokemon"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "battle",
            "trainer",
            "first_pokemon",
            "second_pokemon",
            "third_pokemon",
        ]

    def validate(self, attrs):
        team = [attrs["first_pokemon"], attrs["second_pokemon"], attrs["third_pokemon"]]
        if duplicate_in_set(team):
            raise serializers.ValidationError("Your team has duplicates, please use unique pokemon")
        if pokemon_team_exceeds_limit(team):
            raise serializers.ValidationError(
                "Your team exceeds the 600 points limit, please choose another team"
            )
        return attrs


class DetailBattleSerializer(serializers.ModelSerializer):
    teams = BattleTeamSerializer(many=True, read_only=True)

    class Meta:
        model = Battle
        fields = ["id", "winner", "user_creator", "user_opponent", "teams"]


class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ["user_creator", "user_opponent"]
