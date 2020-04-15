from django.urls import reverse

from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


class TestListPokemonAPI(APITestCase):
    def setUp(self):
        self.pokemon_set = mommy.make("pokemon.Pokemon", _quantity=3)
        self.url = reverse("api:pokemon:list_pokemon")

    def test_list_pokemon(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
