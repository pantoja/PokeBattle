from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.pokemon.serializers import PokemonSerializer
from pokemon.models import Pokemon


class DetailPokemonEndpoint(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class ListPokemonEndpoint(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
