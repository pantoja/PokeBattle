from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from battles.forms import CreateBattleForm, CreateTeamForm
from battles.helpers.common import (
    change_battle_status,
    get_battle_opponent,
    get_respective_teams_in_battle,
)
from battles.helpers.email import send_invite_to_match, send_result_email
from battles.helpers.fight import run_battle
from battles.mixins import UserIsNotInThisBattleMixin, UserNotInvitedToBattleMixin
from battles.models import Battle
from users.models import User


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = CreateBattleForm
    model = Battle

    def get_initial(self):
        return {"user_creator": self.request.user}

    def get_success_url(self):
        return reverse_lazy("battles:create_team", args=[self.object.id])


class CreateTeamView(LoginRequiredMixin, UserNotInvitedToBattleMixin, CreateView):
    template_name = "battles/create_team.html"
    form_class = CreateTeamForm
    success_url = reverse_lazy("home")
    model = Battle

    def get_initial(self):
        battle = Battle.objects.get(pk=self.kwargs["pk"])
        return {"trainer": self.request.user, "battle": battle}

    def get_context_data(self, **kwargs):
        context = super(CreateTeamView, self).get_context_data(**kwargs)

        # If user already created a team for this battle
        user = User.objects.get(id=self.request.user.id)
        battle = self.kwargs["pk"]
        if user.teams.filter(battle=battle).exists():
            context["user_has_team"] = True

        return context

    def form_valid(self, form):
        self.object = form.save()
        battle = self.object.battle
        creator = battle.user_creator
        opponent = battle.user_opponent

        if self.object.trainer == battle.user_creator:
            send_invite_to_match(
                creator.email,
                opponent.email,
                self.request.build_absolute_uri(f"/create-team/{battle.id}"),
            )
        if self.object.trainer == battle.user_opponent:
            result = run_battle(creator.teams.get(battle=battle.pk), self.object)
            change_battle_status(battle, result["winner"].trainer)
            send_result_email(result, self.request.build_absolute_uri("/"))

        return HttpResponseRedirect(self.get_success_url())


class ListSettledBattlesView(LoginRequiredMixin, ListView):
    model = Battle
    template_name = "battles/list_settled_battles.html"

    def get_context_data(self, **kwargs):  # noqa
        context = super().get_context_data(**kwargs)
        user = self.request.user.id
        context["battles"] = Battle.objects.filter(
            Q(user_creator=user) | Q(user_opponent=user), settled=True
        )
        return context


class ListActiveBattlesView(LoginRequiredMixin, ListView):
    model = Battle
    template_name = "battles/list_active_battles.html"

    def get_context_data(self, **kwargs):  # noqa
        context = super().get_context_data(**kwargs)
        user = self.request.user.id
        context["battles"] = Battle.objects.filter(
            Q(user_creator=user) | Q(user_opponent=user), settled=False
        )
        return context


class DetailBattleView(UserIsNotInThisBattleMixin, DetailView):
    model = Battle
    template_name = "battles/detail_battle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        battle = context["battle"]

        opponent = get_battle_opponent(self.request.user, battle)
        context["opponent"] = opponent.get_short_name()

        data = get_respective_teams_in_battle(self.request.user, opponent, battle)
        context.update(data)
        return context
