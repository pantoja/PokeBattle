from django.urls import path

from api.pokemon.views import DetailPokemonAPI


app_name = "pokemon"

urlpatterns = [
    path("pokemon/<int:pk>", DetailPokemonAPI.as_view(), name="detail_pokemon"),
]
