def run_battle(team_1, team_2):  # noqa
    result = []

    result.append(first_round(team_1[0], team_2[0]))
    result.append(second_round(team_1[1], team_2[1]))
    result.append(third_round(team_1[2], team_2[2]))

    if result.count(1) > result.count(2):
        return team_1
    return team_2


def first_round(pkn_1, pkn_2):
    if pkn_1.attack > pkn_2.defense:
        return 1
    return 2


def second_round(pkn_1, pkn_2):
    if pkn_1.defense > pkn_2.attack:
        return 1
    return 2


def third_round(pkn_1, pkn_2):
    if pkn_1.hp > pkn_2.hp:
        return 1
    return 2
