from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from api.battles.serializers import BattleSerializer
from battles.models import Battle


class ListActiveBattlesAPI(ListAPIView):
    serializer_class = BattleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Battle.objects.filter(
            Q(user_creator=user) | Q(user_opponent=user), settled=False
        )
        return queryset


class ListSettledBattlesAPI(ListAPIView):
    serializer_class = BattleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Battle.objects.filter(Q(user_creator=user) | Q(user_opponent=user), settled=True)
        return queryset
