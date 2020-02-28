from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from battles.forms import BattleForm, TeamForm
from battles.models import Battle, Team
from services.api import get_pokemon_list


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = BattleForm
    model = Battle
    success_url = reverse_lazy("create_team")

    def get_initial(self):
        return {"user_creator": self.request.user}


class CreateTeamView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_team.html"
    form_class = TeamForm
    model = Team

    def get_context_data(self, **kwargs):
        context = super(CreateTeamView, self).get_context_data(**kwargs)
        pokemon_list = get_pokemon_list()
        pokemon_list = [p["name"] for p in pokemon_list]
        context["pokemon"] = pokemon_list
        return context
