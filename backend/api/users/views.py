from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.users.serializers import UserSerializer
from users.models import User


class UserSessionEndpoint(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.serializer_class(request.user).data
        return Response(user)


class ListUsersEndpoint(ListAPIView):
    """ Will list all users except the logged one """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.exclude(id=user.id)
        return queryset
