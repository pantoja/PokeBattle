from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email"]
