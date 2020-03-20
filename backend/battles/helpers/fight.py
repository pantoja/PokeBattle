def run_battle(creator_team_object, opponent_team_object):
    result = []
    creator_team = creator_team_object.team.all()
    opponent_team = opponent_team_object.team.all()
    result.append(first_round(creator_team[0], opponent_team[0]))
    result.append(second_round(creator_team[1], opponent_team[1]))
    result.append(third_round(creator_team[2], opponent_team[2]))
    print(result)
    if result.count("creator") > result.count("opponent"):
        return {"winner": creator_team_object, "loser": opponent_team_object}
    return {"winner": opponent_team_object, "loser": creator_team_object}


def first_round(creator_pkn, opponent_pkn):
    if creator_pkn.attack > opponent_pkn.defense:
        return "creator"
    return "opponent"


def second_round(creator_pkn, opponent_pkn):
    if creator_pkn.defense > opponent_pkn.attack:
        return "creator"
    return "opponent"


def third_round(creator_pkn, opponent_pkn):
    if creator_pkn.hp > opponent_pkn.hp:
        return "creator"
    return "opponent"
