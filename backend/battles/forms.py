from django import forms

from battles.models import Battle


class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = [
            "user_opponent",
        ]
