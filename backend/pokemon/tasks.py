import logging

from pokebattle import celery_app
from pokemon.helpers import save_pokemon
from services.api import get_pokemon_list


logger = logging.getLogger(__name__)


@celery_app.task
def save_pokemon_from_pokeapi_weekly():
    logger.info("Saving pokemon from pokeapi")

    pokemon_list = get_pokemon_list()
    pokemon_list = [pokemon["name"] for pokemon in pokemon_list]
    for pokemon in pokemon_list:
        save_pokemon(pokemon)
