import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def pokemon_team_exceeds_limit(team):
    limit = 600
    sum_pokemon_stats = 0
    for pokemon in team:
        stats = sum([pokemon.attack, pokemon.defense, pokemon.hp])
        sum_pokemon_stats += stats
    return sum_pokemon_stats > limit


def duplicate_in_set(item_set):
    return len(item_set) != len(set(item_set))


def change_battle_status(battle, winner):
    battle.settled = True
    battle.winner = winner
    battle.save()


def get_battle_opponent(user, battle):
    if user == battle.user_creator:
        return battle.user_opponent
    return battle.user_creator


def get_respective_teams_in_battle(user, opponent, battle):
    your_team_object = user.teams.get(battle=battle)
    your_team = (
        your_team_object.first_pokemon,
        your_team_object.second_pokemon,
        your_team_object.third_pokemon,
    )

    if battle.settled:
        opponent_team_object = opponent.teams.get(battle=battle)
        opponent_team = (
            opponent_team_object.first_pokemon,
            opponent_team_object.second_pokemon,
            opponent_team_object.third_pokemon,
        )
        return {"winner": battle.winner.get_short_name, "pokemon": zip(your_team, opponent_team)}

    return {"pokemon": zip(your_team, [0, 0, 0])}
