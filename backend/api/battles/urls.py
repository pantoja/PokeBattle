from django.urls import path

from api.battles.views import (
    CreateBattleEndpoint,
    CreateTeamEndpoint,
    DetailBattleEndpoint,
    ListBattlesEndpoint,
)


urlpatterns = [
    path("battles/<status>/", ListBattlesEndpoint.as_view(), name="list_active"),
    path("battle/<pk>/", DetailBattleEndpoint.as_view(), name="detail_battle"),
    path("battle/", CreateBattleEndpoint.as_view(), name="create_battle"),
    path("team/", CreateTeamEndpoint.as_view(), name="create_team"),
]
