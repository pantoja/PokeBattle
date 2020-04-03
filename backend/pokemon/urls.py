from django.urls import path

from pokemon.views import PokemonAutocompleteView


app_name = "pokemon"

urlpatterns = [
    path("pokemon-autocomplete/", PokemonAutocompleteView.as_view(), name="pokemon_autocomplete"),
]
