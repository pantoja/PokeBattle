from templated_email import send_templated_mail


def send_result_email(result):
    winner = result["winner"]
    loser = result["loser"]
    send_templated_mail(
        template_name="send_result",
        from_email="victoria.pantoja@vinta.com.br",
        recipient_list=["vicpantojadoamaral@gmail.com"],  # TODO: use trainer's emails
        context={
            "winner_name": winner.trainer,
            "winner_team": winner.team.all(),
            "loser": loser.trainer,
            "loser_team": loser.team.all(),
        },
    )
