from django.urls import path

from battles.views import CreateBattleView


app_name = "battles"

urlpatterns = [
    path("create/", CreateBattleView.as_view(), name="create_battle"),
]
