from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email_async(user):
    try:
        subject = "Password Changed Successfully"

        html_content = render_to_string("account/pages/mails/change_password.html", {"user": user})

        msg = EmailMultiAlternatives(
            subject=subject,
            body="Your password has been changed successfully",
            to=[user.email],
        )

        msg.attach_alternative(html_content, "text/html")

        msg.send()

    except Exception as e:
        print("Send mail error:", e)
