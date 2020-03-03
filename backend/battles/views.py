from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from battles.forms import CreateBattleForm
from battles.models import Battle


class CreateBattleView(LoginRequiredMixin, CreateView):
    template_name = "battles/create_battle.html"
    form_class = CreateBattleForm
    model = Battle
    success_url = reverse_lazy("home")  # TODO: Change success url to the next step

    def get_initial(self):
        return {"user_creator": self.request.user}
