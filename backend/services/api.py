import requests


def get_pokemon_list():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=50"
    response = requests.get(url)
    response = response.json()
    return response["results"]
