from django.conf import settings

from templated_email import send_templated_mail


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
