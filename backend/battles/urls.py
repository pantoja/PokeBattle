from django.urls import path

from battles.views import CreateBattleView, CreateTeamView, ListSettledBattlesView


app_name = "battles"

urlpatterns = [
    path("create-battle/", CreateBattleView.as_view(), name="create_battle"),
    path("create-team/<int:pk>", CreateTeamView.as_view(), name="create_team"),
    path("settled-battles/", ListSettledBattlesView.as_view(), name="settled_battles"),
]
