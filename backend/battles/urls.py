from django.urls import path

from battles.views import (
    CreateBattleView,
    CreateTeamView,
    DetailBattleView,
    ListActiveBattlesView,
    ListSettledBattlesView,
)


app_name = "battles"

urlpatterns = [
    path("create-battle/", CreateBattleView.as_view(), name="create_battle"),
    path("create-team/<int:pk>", CreateTeamView.as_view(), name="create_team"),
    path("settled-battles/", ListSettledBattlesView.as_view(), name="settled_battles"),
    path("active-battles/", ListActiveBattlesView.as_view(), name="active_battles"),
    path("battle/<int:pk>", DetailBattleView.as_view(), name="detail_battle"),
]
