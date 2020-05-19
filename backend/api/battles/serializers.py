from rest_framework import exceptions, serializers

from api.battles.helpers import order_pokemon_in_team
from api.pokemon.serializers import PokemonSerializer
from api.users.serializers import UserSerializer
from battles.choices import POKEMON_ORDER_CHOICES
from battles.helpers.common import duplicate_in_set, pokemon_team_exceeds_limit
from battles.models import Battle, Team


class DetailTeamSerializer(serializers.ModelSerializer):
    trainer = UserSerializer()
    team = serializers.SerializerMethodField()

    def get_team(self, obj):
        team_set = [obj.first_pokemon, obj.second_pokemon, obj.third_pokemon]
        return PokemonSerializer(team_set, many=True).data

    class Meta:
        model = Team
        fields = ["trainer", "team"]


class CreateTeamSerializer(serializers.ModelSerializer):
    trainer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    choice_1 = serializers.ChoiceField(choices=POKEMON_ORDER_CHOICES, initial=1, write_only=True)
    choice_2 = serializers.ChoiceField(choices=POKEMON_ORDER_CHOICES, initial=2, write_only=True)
    choice_3 = serializers.ChoiceField(choices=POKEMON_ORDER_CHOICES, initial=3, write_only=True)

    class Meta:
        model = Team
        fields = [
            "battle",
            "trainer",
            "first_pokemon",
            "second_pokemon",
            "third_pokemon",
            "choice_1",
            "choice_2",
            "choice_3",
        ]

    def validate(self, attrs):
        team = (attrs["first_pokemon"], attrs["second_pokemon"], attrs["third_pokemon"])
        choices = (attrs["choice_1"], attrs["choice_2"], attrs["choice_3"])

        if attrs["trainer"] not in (attrs["battle"].user_creator, attrs["battle"].user_opponent):
            raise exceptions.NotFound()
        if duplicate_in_set(team):
            raise serializers.ValidationError("Your team has duplicates, please use unique pokemon")
        if duplicate_in_set(choices):
            raise serializers.ValidationError("Please allocate one pokemon per round")
        if pokemon_team_exceeds_limit(team):
            raise serializers.ValidationError(
                "Your team exceeds the 600 points limit, please choose another team"
            )
        attrs = order_pokemon_in_team(attrs)
        return attrs


class DetailBattleSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()
    opponent = serializers.SerializerMethodField()
    winner = serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%d/%m/%y")

    def get_winner(self, obj):
        if not obj.winner:
            return None
        return obj.winner.email

    def get_creator(self, obj):
        team = obj.teams.get(trainer=obj.user_creator)
        serializer = DetailTeamSerializer(team)
        return serializer.data

    def get_opponent(self, obj):
        if not obj.settled:
            return {"trainer": UserSerializer(obj.user_opponent).data, "team": None}
        team = obj.teams.get(trainer=obj.user_opponent)
        serializer = DetailTeamSerializer(team)
        return serializer.data

    class Meta:
        model = Battle
        fields = ["id", "winner", "created", "creator", "opponent"]


class CreateBattleSerializer(serializers.ModelSerializer):
    user_creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Battle
        fields = ["user_creator", "user_opponent"]

    def validate(self, attrs):
        if self.context["request"].user == attrs["user_opponent"]:
            raise serializers.ValidationError("You can't battle yourself")
        return attrs
