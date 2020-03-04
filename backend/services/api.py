import requests


def get_pokemon_list():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=50"
    response = requests.get(url)
    response = response.json()
    return response["results"]


def get_pokemon_stats(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
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
