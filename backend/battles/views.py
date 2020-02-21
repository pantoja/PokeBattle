from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from battles.forms import BattleForm
from battles.models import Battle


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = BattleForm
    model = Battle
    success_url = reverse_lazy("home")  # TODO: Change success url to the next step
