from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from battles.forms import CreateBattleForm, CreateTeamForm
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

        # Determine if you are opponent or creator
        battle = context["battle"]
        if self.request.user == battle.user_creator:
            opponent = battle.user_opponent
        else:
            opponent = battle.user_creator

        context["opponent"] = opponent.get_short_name
        your_team_object = self.request.user.teams.get(battle=battle)
        your_team = (
            your_team_object.first_pokemon,
            your_team_object.second_pokemon,
            your_team_object.third_pokemon,
        )

        # Battle is settled
        if battle.settled:
            context["winner"] = battle.winner.get_short_name
            opponent_team_object = opponent.teams.get(battle=battle)
            opponent_team = (
                opponent_team_object.first_pokemon,
                opponent_team_object.second_pokemon,
                opponent_team_object.third_pokemon,
            )
            context["pokemon"] = zip(your_team, opponent_team)

            return context

        # Battle is not settled
        context["pokemon"] = zip(your_team, [0, 0, 0])
        return context
