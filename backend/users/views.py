from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserSignUpForm
from users.models import User


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "users/sign-up.html"
    success_url = reverse_lazy("home")
