from django import forms

from battles.models import Battle, Team
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


class TeamForm(forms.ModelForm):
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
