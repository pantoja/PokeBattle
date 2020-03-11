from django import forms

from battles.helpers import duplicate_pokemon, pokemon_attr_exceeds_limit
from battles.models import Battle, Team
from services.api import POKE_API_LIMIT
from users.models import User


class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = [
            "user_creator",
            "user_opponent",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_opponent"].queryset = User.objects.exclude(
            id=self.initial["user_creator"].id
        )


class CreateTeamForm(forms.ModelForm):
    pokemon_1 = forms.IntegerField()
    pokemon_2 = forms.IntegerField()
    pokemon_3 = forms.IntegerField()

    class Meta:
        model = Team
        fields = ["trainer", "pokemon_1", "pokemon_2", "pokemon_3"]

    def save(self, commit=True):
        # Saves Team object
        trainer = self.cleaned_data["trainer"]

        pokemon_1 = self.cleaned_data["pokemon_1"]
        pokemon_2 = self.cleaned_data["pokemon_2"]
        pokemon_3 = self.cleaned_data["pokemon_3"]

        team = (pokemon_1, pokemon_2, pokemon_3)
        instance = Team.objects.create(trainer=trainer, battle=self.initial["battle"])
        instance.team.set(team)
        return instance

    def clean(self):

        cleaned_data = super().clean()

        pokemon_1 = cleaned_data.get("pokemon_1")
        pokemon_2 = cleaned_data.get("pokemon_2")
        pokemon_3 = cleaned_data.get("pokemon_3")

        team = (pokemon_1, pokemon_2, pokemon_3)

        for pokemon in team:
            if pokemon < 0 or pokemon > POKE_API_LIMIT:
                raise forms.ValidationError("Choose a valid pokemon")

        if duplicate_pokemon(team):
            raise forms.ValidationError("Your team has duplicates, please use unique ids")

        if not pokemon_attr_exceeds_limit(team):
            raise forms.ValidationError(
                "Your team exceeds the 600 points limit, please choose another team"
            )

        return cleaned_data
