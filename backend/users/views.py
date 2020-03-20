from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import User


class UserSignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "users/sign-up.html"
    success_url = reverse_lazy("home")
