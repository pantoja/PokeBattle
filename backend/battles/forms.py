from django import forms

from dal import autocomplete

from battles.choices import POKEMON_ORDER_CHOICES
from battles.helpers.common import (
    change_battle_status,
    duplicate_in_set,
    pokemon_team_exceeds_limit,
)
from battles.helpers.email import send_result_email
from battles.helpers.fight import run_battle
from battles.models import Battle, Team
from pokemon.models import Pokemon
from users.models import User


class CreateBattleForm(forms.ModelForm):
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
    pokemon_1 = forms.ModelChoiceField(
        queryset=Pokemon.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="pokemon:pokemon_autocomplete", attrs={"data-html": True}
        ),
    )
    pokemon_2 = forms.ModelChoiceField(
        queryset=Pokemon.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="pokemon:pokemon_autocomplete", attrs={"data-html": True}
        ),
    )
    pokemon_3 = forms.ModelChoiceField(
        queryset=Pokemon.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="pokemon:pokemon_autocomplete", attrs={"data-html": True}
        ),
    )

    order_1 = forms.ChoiceField(choices=POKEMON_ORDER_CHOICES, initial=1)
    order_2 = forms.ChoiceField(choices=POKEMON_ORDER_CHOICES, initial=2)
    order_3 = forms.ChoiceField(choices=POKEMON_ORDER_CHOICES, initial=3)

    class Meta:
        model = Team
        fields = ["trainer", "pokemon_1", "pokemon_2", "pokemon_3", "order_1", "order_2", "order_3"]

    def save(self, commit=True):
        # Saves Team object
        trainer = self.cleaned_data["trainer"]

        pokemon_1 = self.cleaned_data["pokemon_1"]
        pokemon_2 = self.cleaned_data["pokemon_2"]
        pokemon_3 = self.cleaned_data["pokemon_3"]

        order_1 = self.cleaned_data["order_1"]
        order_2 = self.cleaned_data["order_2"]
        order_3 = self.cleaned_data["order_3"]

        battle_order = {
            order_1: pokemon_1,
            order_2: pokemon_2,
            order_3: pokemon_3,
        }

        instance = Team.objects.create(
            trainer=trainer,
            battle=self.initial["battle"],
            first_pokemon=battle_order["1"],
            second_pokemon=battle_order["2"],
            third_pokemon=battle_order["3"],
        )

        # Runs battle

        battle = Battle.objects.get(pk=self.initial["battle"].pk)
        creator = battle.user_creator
        opponent = battle.user_opponent
        if trainer == opponent:
            result = run_battle(creator.teams.get(battle=battle.pk), instance)
            change_battle_status(battle, result["winner"].trainer)
            send_result_email(result)
        return instance

    def clean(self):

        cleaned_data = super().clean()

        pokemon_1 = cleaned_data.get("pokemon_1")
        pokemon_2 = cleaned_data.get("pokemon_2")
        pokemon_3 = cleaned_data.get("pokemon_3")

        team = (pokemon_1, pokemon_2, pokemon_3)

        order_1 = self.cleaned_data["order_1"]
        order_2 = self.cleaned_data["order_2"]
        order_3 = self.cleaned_data["order_3"]

        order = (order_1, order_2, order_3)

        if duplicate_in_set(order):
            raise forms.ValidationError("Please allocate one pokemon per round")

        if duplicate_in_set(team):
            raise forms.ValidationError("Your team has duplicates, please use unique pokemon")

        if pokemon_team_exceeds_limit(team):
            raise forms.ValidationError(
                "Your team exceeds the 600 points limit, please choose another team"
            )

        return cleaned_data
