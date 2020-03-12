from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from battles.forms import BattleForm, CreateTeamForm
from battles.helpers import save_pokemon_in_team
from battles.models import Battle
from services.api import get_pokemon_list
from users.models import User


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = BattleForm
    model = Battle

    def get_initial(self):
        return {"user_creator": self.request.user}

    def get_success_url(self):
        return reverse_lazy("battles:create_team", args=[self.object.id])


class CreateTeamView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_team.html"
    form_class = CreateTeamForm
    success_url = reverse_lazy("home")

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
