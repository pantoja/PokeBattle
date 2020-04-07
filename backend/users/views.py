from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.email import send_signup_invite_email
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


class InviteFriendView(LoginRequiredMixin, FormView):
    form_class = InviteFriendForm
    template_name = "users/invite_friend.html"

    def form_valid(self, form):
        invitee = self.request.user.email
        invited = form.cleaned_data.get("email")
        url = self.request.build_absolute_uri("/")
        send_signup_invite_email(invitee, invited, url)
        messages.success(self.request, "Your invitation was sent!")
        return HttpResponseRedirect("/invite")
