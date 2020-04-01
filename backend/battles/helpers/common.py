import logging

from django.core.exceptions import PermissionDenied

from battles.models import Team
from services.api import get_pokemon_stats


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def pokemon_team_exceeds_limit(team):
    limit = 600

    team_stats = [get_pokemon_stats(pokemon) for pokemon in team]
    sum_pokemon_stats = []

    for pokemon in team_stats:
        sum_pokemon_stats.append(sum([pokemon["attack"], pokemon["defense"], pokemon["hp"]]))

    return sum(sum_pokemon_stats) > limit


def duplicate_in_set(item_set):
    return len(item_set) != len(set(item_set))


def change_battle_status(battle, winner):
    if not len(Team.objects.filter(battle=battle.id)) == 2:
        logger.error("Battle did not save both teams")
        raise PermissionDenied
    battle.settled = True
    battle.winner = winner
    battle.save()
