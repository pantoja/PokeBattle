from django.urls import path

from api.users.views import ListUsersEndpoint, UserSessionEndpoint


app_name = "battle"

urlpatterns = [
    path("user/", UserSessionEndpoint.as_view(), name="detail-user"),
    path("users/", ListUsersEndpoint.as_view(), name="list-users"),
]
