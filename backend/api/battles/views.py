from django.db.models import Q

from rest_framework import exceptions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.battles.permissions import IsInBattle
from api.battles.serializers import (
    CreateBattleSerializer,
    CreateTeamSerializer,
    DetailBattleSerializer,
    ListBattleSerializer,
)
from battles.models import Battle, Team


class ListBattlesView(ListAPIView):
    serializer_class = ListBattleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status = self.kwargs["status"]
        # TODO: Create manager
        queryset = Battle.objects.filter(
            Q(user_creator=user) | Q(user_opponent=user), settled=status == "settled"
        )
        return queryset

    def dispatch(self, request, *args, **kwargs):
        status = self.kwargs["status"]
        if status not in ["settled", "active"]:
            raise exceptions.ValidationError("This status in non-existant")
        return super().dispatch(request, *args, **kwargs)


class DetailBattleView(RetrieveAPIView):
    serializer_class = DetailBattleSerializer
    queryset = Battle.objects.all()
    permission_classes = [IsInBattle]


class CreateBattleView(CreateAPIView):
    serializer_class = CreateBattleSerializer
    permission_classes = [IsAuthenticated]


class CreateTeamView(CreateAPIView):
    serializer_class = CreateTeamSerializer
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
