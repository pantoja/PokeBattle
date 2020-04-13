from django.conf import settings

from templated_email import send_templated_mail


def send_signup_invite_email(invitee, invited, url):
    send_templated_mail(
        template_name="signup_invitation",
        from_email=settings.SERVER_EMAIL,
        recipient_list=[invited],
        context={"invitee": invitee, "invited": invited, "url": url},
    )
