from typing import override

import boto3

from mail.services.base import EmailService


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
        destination = {
            "ToAddresses": to_emails,
        }

        if cc_emails:
            destination["CcAddresses"] = cc_emails

        if bcc_email:
            destination["BccAddresses"] = bcc_email

        self.ses_client.send_email(
            Source="sender@example.com",
            Destination=destination,
            Message={
                "Subject": {"Data": self.subject},
                "Body": {
                    "Text": {"Data": html_content},
                    "Html": {"Data": html_content},
                },
            },
        )
