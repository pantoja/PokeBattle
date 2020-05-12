from django.urls import path

from api.pokemon.views import DetailPokemonEndpoint, ListPokemonEndpoint


app_name = "pokemon"

urlpatterns = [
    path("pokemon/<int:pk>", DetailPokemonEndpoint.as_view(), name="detail_pokemon"),
    path("pokemon/", ListPokemonEndpoint.as_view(), name="list_pokemon"),
]
