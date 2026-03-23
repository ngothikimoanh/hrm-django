from abc import ABC, abstractmethod
from typing import Any

from django.template.loader import render_to_string


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
