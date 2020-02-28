from django.urls import path

from battles.views import CreateBattleView, CreateTeamView


app_name = "battles"

urlpatterns = [
    path("create-battle/", CreateBattleView.as_view(), name="create_battle"),
    path("create-team/", CreateTeamView.as_view(), name="create_team"),
]
