from django.db.models import Q

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.battles.permissions import IsInBattle
from api.battles.serializers import (
    BattleSerializer,
    DetailBattleSerializer,
    ListBattleSerializer,
    TeamSerializer,
)
from battles.models import Battle, Team


class ListActiveBattlesView(ListAPIView):
    serializer_class = ListBattleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Battle.objects.filter(
            Q(user_creator=user) | Q(user_opponent=user), settled=False
        )
        return queryset


class ListSettledBattlesView(ListAPIView):
    serializer_class = ListBattleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Battle.objects.filter(Q(user_creator=user) | Q(user_opponent=user), settled=True)
        return queryset


class DetailBattleView(RetrieveAPIView):
    serializer_class = DetailBattleSerializer
    queryset = Battle.objects.all()
    permission_classes = [IsInBattle]


class CreateBattleView(CreateAPIView):
    serializer_class = BattleSerializer
    permission_classes = [IsAuthenticated]


class CreateTeamView(CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
