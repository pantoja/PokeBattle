import logging

from django.conf import settings

from templated_email import send_templated_mail


logger = logging.getLogger(__name__)


def send_result_email(result):
    winner = result["winner"]
    loser = result["loser"]
    send_templated_mail(
        template_name="send_result",
        from_email=settings.SERVER_EMAIL,
        recipient_list=[winner.trainer.email, loser.trainer.email],
        context={
            "winner": winner.trainer,
            "winner_team": (winner.first_pokemon, winner.second_pokemon, winner.third_pokemon),
            "loser": loser.trainer,
            "loser_team": (loser.first_pokemon, loser.second_pokemon, loser.third_pokemon),
        },
    )


def send_invite_to_match(invitee, invited):
    send_templated_mail(
        template_name="invite_to_battle",
        from_email=settings.SERVER_EMAIL,
        recipient_list=[invited],
        context={"invitee": invitee, "invited": invited},
    )
    logger.info("Sent email invite to battle")
