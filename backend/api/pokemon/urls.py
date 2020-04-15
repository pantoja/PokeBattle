from django.urls import path

from api.pokemon.views import DetailPokemonAPI, ListPokemonAPI


urlpatterns = [
    path("pokemon/", ListPokemonAPI.as_view(), name="list_pokemon"),
    path("pokemon/<int:pk>", DetailPokemonAPI.as_view(), name="detail_pokemon"),
]
