from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from account.mail.base_mail import EmailSMTPService

EmailBaseClass = EmailSMTPService


class ChangePasswordEmail(EmailBaseClass):
    subject: str = "Password Changed Successfully"
    template_name: str = "account/pages/mail/change_password.html"

    def send(self, user):
        html_content = render_to_string(self.template_name, {"user": user})

        msg = EmailMultiAlternatives(
            subject=self.subject,
            body="Your password has been changed successfully",
            to=[user.email],
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()
