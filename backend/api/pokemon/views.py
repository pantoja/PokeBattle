from rest_framework.generics import RetrieveAPIView

from api.pokemon.serializers import PokemonSerializer
from pokemon.models import Pokemon


class DetailPokemonEndpoint(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
