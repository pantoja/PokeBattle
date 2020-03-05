from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from battles.forms import BattleForm, TeamForm
from battles.helpers import save_pokemon_in_team
from battles.models import Battle
from services.api import get_pokemon_list


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = BattleForm
    model = Battle

    def get_initial(self):
        return {"user_creator": self.request.user}

    def get_success_url(self):
        self.success_url = reverse_lazy("battles:create_team", args=[self.object.id])
        return self.success_url


class CreateTeamView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_team.html"
    form_class = TeamForm
    success_url = reverse_lazy("home")

    def get_initial(self):
        battle = Battle.objects.get(pk=self.kwargs["pk"])
        return {"trainer": self.request.user, "battle": battle}

    def get_context_data(self, **kwargs):
        context = super(CreateTeamView, self).get_context_data(**kwargs)
        pokemon_list = get_pokemon_list()
        pokemon_list = [p["name"] for p in pokemon_list]
        context["pokemon"] = pokemon_list
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
