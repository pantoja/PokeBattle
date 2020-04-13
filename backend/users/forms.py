from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email"]


class InviteFriendForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This user already has an account")
        return self.cleaned_data
