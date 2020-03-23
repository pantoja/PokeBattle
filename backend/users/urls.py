from django.urls import path

from users.views import UserSignUpView


app_name = "users"

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="signup"),
]
