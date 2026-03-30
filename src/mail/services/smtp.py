from typing import override

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from mail.services.base import EmailService


class EmailSMTPService(EmailService):
    @override
    def send_mail(
        self,
        to_emails: list[str],
        html_content: str,
        cc_emails: list[str] | None = None,
        bcc_email: list[str] | None = None,
    ) -> None:
        msg = EmailMultiAlternatives(
            subject=self.subject,
            body=html_content,
            from_email=settings.FROM_EMAIL,
            to=to_emails,
            cc=cc_emails,
            bcc=bcc_email,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
