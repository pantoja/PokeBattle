from django.db.models import Count

from rest_framework import exceptions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.battles.permissions import IsInBattle
from api.battles.serializers import (
    CreateBattleSerializer,
    CreateTeamSerializer,
    DetailBattleSerializer,
)
from battles.models import Battle, Team


class ListBattlesEndpoint(ListAPIView):
    serializer_class = DetailBattleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status = self.kwargs["status"]
        queryset = Battle.objects.filter_by_status(user, status == "settled")
        if status == "settled":
            # Return only battles with two teams
            return queryset.annotate(num_teams=Count("teams")).filter(num_teams__gt=1)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        status = self.kwargs["status"]
        if status not in ["settled", "active"]:
            raise exceptions.ValidationError("This status in non-existant")
        return super().dispatch(request, *args, **kwargs)


class DetailBattleEndpoint(RetrieveAPIView):
    serializer_class = DetailBattleSerializer
    queryset = Battle.objects.all()
    permission_classes = [IsInBattle]


class CreateBattleEndpoint(CreateAPIView):
    serializer_class = CreateBattleSerializer
    permission_classes = [IsAuthenticated]


class CreateTeamEndpoint(CreateAPIView):
    serializer_class = CreateTeamSerializer
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
