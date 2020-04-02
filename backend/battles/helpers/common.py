import logging

from django.core.exceptions import PermissionDenied

from battles.models import Team
from services.api import get_pokemon_stats


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def pokemon_team_exceeds_limit(team):
    limit = 600

    team_stats = [get_pokemon_stats(pokemon.name) for pokemon in team]
    sum_pokemon_stats = []

    for pokemon in team_stats:
        sum_pokemon_stats.append(sum([pokemon["attack"], pokemon["defense"], pokemon["hp"]]))

    return sum(sum_pokemon_stats) > limit


def duplicate_pokemon(team):
    for pokemon in team:
        if team.count(pokemon) > 1:
            return True
    return False


def change_battle_status(battle, winner):
    if not len(Team.objects.filter(battle=battle.id)) == 2:
        logger.error("Battle did not save both teams")
        raise PermissionDenied
    battle.settled = True
    battle.winner = winner
    battle.save()


def get_battle_opponent(user, battle):
    if user == battle.user_creator:
        return battle.user_opponent
    return battle.user_creator


def get_respective_teams_in_battle(user, opponent, battle):
    your_team = user.teams.get(battle=battle).team.all()

    if battle.settled:
        opponent_team = opponent.teams.get(battle=battle).team.all()
        return {"winner": battle.winner.get_short_name, "pokemon": zip(your_team, opponent_team)}

    return {"pokemon": zip(your_team, [0, 0, 0])}
