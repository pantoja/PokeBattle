from dal import autocomplete

from pokemon.models import Pokemon


class PokemonAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Pokemon.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
