from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class UserIsNotInThisBattleMixin(UserPassesTestMixin):
    permission_denied_message = "You are not allowed in this page"

    def test_func(self):
        battle_object = self.get_object()
        if battle_object.settled:
            return self.request.user in [battle_object.user_creator, battle_object.user_opponent]
        return battle_object.user_creator == self.request.user

    def handle_no_permission(self):
        return redirect("home")


class UserNotInvitedToBattleMixin(UserPassesTestMixin):
    def test_func(self):
        battle_object = self.get_object()
        return self.request.user in [battle_object.user_creator, battle_object.user_opponent]

    def handle_no_permission(self):
        return redirect("home")
