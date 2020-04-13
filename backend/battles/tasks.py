from celery.utils.log import get_task_logger

from battles.helpers.common import change_battle_status
from battles.helpers.email import send_result_email
from battles.helpers.fight import run_battle
from battles.models import Battle, Team
from pokebattle import celery_app


logger = get_task_logger(__name__)


@celery_app.task
def run_battle_task(pk, url):
    #  Using %s because pylint raises a formatting error
    logger.info("Running battle number %s", pk)
    battle = Battle.objects.get(pk=pk)
    result = run_battle(
        Team.objects.get(battle=pk, trainer=battle.user_creator),
        Team.objects.get(battle=pk, trainer=battle.user_opponent),
    )
    change_battle_status(battle, result["winner"].trainer)
    send_result_email(result, url)
