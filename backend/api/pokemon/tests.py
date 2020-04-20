from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from api.pokemon.serializers import PokemonSerializer


class TestListPokemonAPI(APITestCase):
    def setUp(self):
        self.pokemon = mommy.make("pokemon.Pokemon", id=1)
        self.url = "/api/pokemon/1"

    def test_detail_pokemon(self):
        response = self.client.get(self.url)
        pokemon = PokemonSerializer(self.pokemon)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, pokemon.data)

    def test_pokemon_not_exist(self):
        response = self.client.get("api/pokemon/2")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
