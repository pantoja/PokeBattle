from django.utils.html import format_html

from dal import autocomplete

from pokemon.models import Pokemon


class PokemonAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Pokemon.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

    def get_result_label(self, item):  # noqa
        return format_html(f'<img src="{item.sprite}"> {item}')

    def get_selected_result_label(self, result):
        return result.name.capitalize()
