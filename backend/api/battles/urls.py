from django.urls import path

from api.battles.views import CreateBattleView, CreateTeamView, DetailBattleView, ListBattlesView


app_name = "battle"

urlpatterns = [
    path("battles/<status>/", ListBattlesView.as_view(), name="list_active"),
    path("battle/<pk>/", DetailBattleView.as_view(), name="detail_battle"),
    path("battle/", CreateBattleView.as_view(), name="create_battle"),
    path("team/", CreateTeamView.as_view(), name="create_team"),
]
