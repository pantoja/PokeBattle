from pokemon.models import Pokemon
from services.api import get_pokemon_stats


def save_pokemon_in_team(selected_team):
    for pokemon in selected_team:
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


def pokemon_attr_exceeds_limit(team):
    limit = 600

    team_data = [get_pokemon_stats(pokemon) for pokemon in team]
    pkn_points = []

    for pkn_data in team_data:
        pkn_points.append(sum([pkn_data["attack"], pkn_data["defense"], pkn_data["hp"]]))
    return sum(pkn_points) < limit


def duplicate_pokemon(team):
    for pokemon in team:
        if team.count(pokemon) > 1:
            return True
    return False
