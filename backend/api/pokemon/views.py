from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.pokemon.serializers import PokemonSerializer
from pokemon.models import Pokemon


class ListPokemonAPI(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class DetailPokemonAPI(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
