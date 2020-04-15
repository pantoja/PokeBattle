from django.urls import path

from api.battles.views import ListActiveBattlesAPI, ListSettledBattlesAPI


app_name = "battle"

urlpatterns = [
    path("battles/active", ListActiveBattlesAPI.as_view(), name="list_active"),
    path("battles/settled", ListSettledBattlesAPI.as_view(), name="list_settled"),
]
