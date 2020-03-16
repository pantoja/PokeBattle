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


def pokemon_team_exceeds_limit(team):
    limit = 600

    team_stats = [get_pokemon_stats(pokemon) for pokemon in team]
    sum_pokemon_stats = []

    for pokemon in team_stats:
        sum_pokemon_stats.append(sum([pokemon["attack"], pokemon["defense"], pokemon["hp"]]))

    return sum(sum_pokemon_stats) > limit


def duplicate_pokemon(team):
    for pokemon in team:
        if team.count(pokemon) > 1:
            return True
    return False
