from rest_framework import serializers

from pokemon.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name.capitalize()

    class Meta:
        model = Pokemon
        fields = ["id", "name", "sprite", "attack", "defense", "hp"]
