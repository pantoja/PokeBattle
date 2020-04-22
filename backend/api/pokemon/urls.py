from django.urls import path

from api.pokemon.views import DetailPokemonEndpoint


app_name = "pokemon"

urlpatterns = [
    path("pokemon/<int:pk>", DetailPokemonEndpoint.as_view(), name="detail_pokemon"),
]
