from rest_framework.permissions import BasePermission


class IsInBattle(BasePermission):
    def has_object_permission(self, request, view, obj):
        if len(obj.teams.all()) == 1:
            return request.user == obj.user_creator
        return request.user in [obj.user_creator, obj.user_opponent]
