from django.urls import path

from users.views import InviteFriendView, UserLoginView, UserLogoutView, UserSignUpView


app_name = "users"

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("invite/", InviteFriendView.as_view(), name="invite_friend"),
]
