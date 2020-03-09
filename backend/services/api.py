import requests


POKEAPI_ROOT_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_list():
    response = requests.get(f"{POKEAPI_ROOT_URL}?limit=50")
    if not response.ok:
        return None
    return response.json()["results"]


def get_pokemon_stats(pokemon):
    response = requests.get(f"{POKEAPI_ROOT_URL}{pokemon}")
    if not response.ok:
        return None
    response = response.json()
    data = {
        "name": response["forms"][0]["name"],
        "id": response["id"],
        "sprite": response["sprites"]["front_default"],
        "attack": response["stats"][4]["base_stat"],
        "defense": response["stats"][3]["base_stat"],
        "hp": response["stats"][5]["base_stat"],
    }
    return data
