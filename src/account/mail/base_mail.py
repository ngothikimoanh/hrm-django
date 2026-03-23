from abc import ABC, abstractmethod
from typing import Any, override

import boto3
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from main import settings


class EmailService(ABC):
    template_name: str
    subject: str

    def generate_html(self, context: dict[str, Any]):
        return render_to_string(template_name=self.template_name, context=context)

    @abstractmethod
    def send_mail(
        self,
        to_emails: list[str],
        html_content: str,
        cc_emails: list[str] | None = None,
        bcc_email: list[str] | None = None,
    ) -> None: ...


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


class MailSESService(EmailService):
    ses_client = boto3.client("ses", region_name="us-east-1")

    @override
    def send_mail(
        self,
        to_emails: list[str],
        html_content: str,
        cc_emails: list[str] | None = None,
        bcc_email: list[str] | None = None,
    ) -> None:
        self.ses_client.send_email(
            Source="sender@example.com",
            Destination={
                "ToAddresses": to_emails,
            },
            Message={
                "Subject": {"Data": self.subject},
                "Body": {"Text": {"Data": html_content}, "Html": {"Data": html_content}},
            },
        )
