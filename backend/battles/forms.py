from django import forms

from battles.models import Battle
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
