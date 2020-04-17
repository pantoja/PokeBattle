from rest_framework import exceptions, serializers

from api.pokemon.serializers import PokemonSerializer
from battles.helpers.common import duplicate_in_set, pokemon_team_exceeds_limit
from battles.models import Battle, Team


# from battles.choices import POKEMON_ORDER_CHOICES


class ListBattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ["id", "settled", "winner", "user_creator", "user_opponent"]


class BattleTeamSerializer(serializers.ModelSerializer):
    first_pokemon = PokemonSerializer()
    second_pokemon = PokemonSerializer()
    third_pokemon = PokemonSerializer()
    trainer = serializers.SerializerMethodField()

    def get_trainer(self, obj):
        return obj.trainer.email

    class Meta:
        model = Team
        fields = ["trainer", "first_pokemon", "second_pokemon", "third_pokemon"]


# TODO: add choice fields
class TeamSerializer(serializers.ModelSerializer):
    # choice_1 = serializers.ChoiceField(choices=POKEMON_ORDER_CHOICES, write_only=True)
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
        if attrs["trainer"] not in [attrs["battle"].user_creator, attrs["battle"].user_opponent]:
            raise exceptions.NotFound()
        if duplicate_in_set(team):
            raise serializers.ValidationError("Your team has duplicates, please use unique pokemon")
        if pokemon_team_exceeds_limit(team):
            raise serializers.ValidationError(
                "Your team exceeds the 600 points limit, please choose another team"
            )
        return attrs


class DetailBattleSerializer(serializers.ModelSerializer):
    creator_team = serializers.SerializerMethodField()
    opponent_team = serializers.SerializerMethodField()
    winner = serializers.SerializerMethodField()

    def get_winner(self, obj):
        return obj.winner.email

    def get_creator_team(self, obj):
        team = Team.objects.get(battle=obj, trainer=obj.user_creator)
        serializer = BattleTeamSerializer(team)
        return serializer.data

    def get_opponent_team(self, obj):
        team = Team.objects.get(battle=obj, trainer=obj.user_opponent)
        serializer = BattleTeamSerializer(team)
        return serializer.data

    class Meta:
        model = Battle
        fields = ["id", "winner", "creator_team", "opponent_team"]


class CreateBattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ["user_creator", "user_opponent"]
