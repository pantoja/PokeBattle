from django.urls import path

from users.views import UserSignUpView


app_name = "users"

urlpatterns = [path("sign-up/", UserSignUpView.as_view(), name="sign-up")]
