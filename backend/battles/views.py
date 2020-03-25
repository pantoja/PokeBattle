from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from battles.forms import CreateBattleForm, CreateTeamForm
from battles.helpers.common import save_pokemon_in_team
from battles.mixins import UserIsNotInThisBattleMixin
from battles.models import Battle
from services.api import get_pokemon_list
from users.models import User


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = CreateBattleForm
    model = Battle

    def get_initial(self):
        return {"user_creator": self.request.user}

    def get_success_url(self):
        return reverse_lazy("battles:create_team", args=[self.object.id])


class CreateTeamView(LoginRequiredMixin, UserIsNotInThisBattleMixin, CreateView):
    template_name = "battles/create_team.html"
    form_class = CreateTeamForm
    success_url = reverse_lazy("home")
    model = Battle

    def get_initial(self):
        battle = Battle.objects.get(pk=self.kwargs["pk"])
        return {"trainer": self.request.user, "battle": battle}

    def get_context_data(self, **kwargs):
        context = super(CreateTeamView, self).get_context_data(**kwargs)

        # Add pokemon dropdown
        pokemon_list = get_pokemon_list()
        pokemon_list = [p["name"] for p in pokemon_list]
        context["pokemon"] = pokemon_list

        # If user already created a team for this battle
        user = User.objects.get(id=self.request.user.id)
        battle = self.kwargs["pk"]
        if user.teams.filter(battle=battle).exists():
            context["user_has_team"] = True

        return context

    def form_valid(self, form):
        # Saves unsaved pokemon

        pokemon_1 = form.cleaned_data["pokemon_1"]
        pokemon_2 = form.cleaned_data["pokemon_2"]
        pokemon_3 = form.cleaned_data["pokemon_3"]

        selected_team = [pokemon_1, pokemon_2, pokemon_3]
        save_pokemon_in_team(selected_team)

        self.object = form.save()
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
        if self.request.user == battle.user_creator:
            opponent = battle.user_opponent
        else:
            opponent = battle.user_creator

        context["opponent"] = opponent.get_short_name
        your_team = self.request.user.teams.get(battle=battle).team.all()

        winner = battle.winner
        if winner:
            context["winner"] = winner.get_short_name
            opponent_team = opponent.teams.get(battle=battle).team.all()
            context["pokemon"] = zip(your_team, opponent_team)
            return context

        context["pokemon"] = zip(your_team, [0, 0, 0])
        return context
