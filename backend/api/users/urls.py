from django.urls import path

from api.users.views import UserSessionEndpoint


app_name = "battle"

urlpatterns = [
    path("user/", UserSessionEndpoint.as_view(), name="detail-user"),
]
