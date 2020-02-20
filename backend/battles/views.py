from django.views.generic import FormView

from battles.forms import BattleForm


class CreateBattleView(FormView):
    template_name = "battles/create_battle.html"
    form_class = BattleForm
