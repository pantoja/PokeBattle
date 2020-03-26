from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class UserIsNotInThisBattleMixin(UserPassesTestMixin):
    permission_denied_message = "You are not allowed in this page"

    def test_func(self):
        if self.get_object().settled:
            return (
                self.get_object().user_creator == self.request.user
                or self.get_object().user_opponent == self.request.user
            )
        return self.get_object().user_creator == self.request.user

    def handle_no_permission(self):
        return redirect("home")


class UserNotInvitedToBattleMixin(UserPassesTestMixin):
    def test_func(self):
        return (
            self.get_object().user_creator == self.request.user
            or self.get_object().user_opponent == self.request.user
        )

    def handle_no_permission(self):
        return redirect("home")
