from django.forms import ModelForm

from users.models import User


class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ["email"]
