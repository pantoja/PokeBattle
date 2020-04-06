from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.forms import InviteFriendForm, UserSignUpForm
from users.models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    pass


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class InviteFriendView(FormView):
    form_class = InviteFriendForm
    template_name = "users/invite_friend.html"
    success_url = reverse_lazy("home")
