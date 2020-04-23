def order_pokemon_in_team(attrs):
    rounds = {
        attrs["choice_1"]: attrs["first_pokemon"],
        attrs["choice_2"]: attrs["second_pokemon"],
        attrs["choice_3"]: attrs["third_pokemon"],
    }

    attrs.update(first_pokemon=rounds[1], second_pokemon=rounds[2], third_pokemon=rounds[3])

    attrs.pop("choice_1")
    attrs.pop("choice_2")
    attrs.pop("choice_3")

    return attrs
