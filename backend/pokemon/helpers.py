from pokemon.models import Pokemon
from services.api import get_pokemon_stats


def save_pokemon(pokemon):
    if not Pokemon.objects.filter(id=pokemon).exists():
        data = get_pokemon_stats(pokemon)
        Pokemon.objects.create(
            name=data["name"],
            id=data["id"],
            sprite=data["sprite"],
            attack=data["attack"],
            defense=data["defense"],
            hp=data["hp"],
        )
