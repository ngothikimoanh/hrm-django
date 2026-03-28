from typing import override

from django.utils import timezone

from account.models.verify_email import EmailVerifyToken
from account.services.email_verify.base import EmailVerify


class LinkVerifier(EmailVerify):
    def __init__(self, token: str):
        self.token = token
        self.email_verify_token: EmailVerifyToken | None = None

    @override
    def clean(self):
        pass

    @override
    def is_valid(self) -> bool:
        self.email_verify_token = EmailVerifyToken.objects.filter(token=self.token).first()

        if self.email_verify_token is None:
            return False

        if self.email_verify_token.expired_at > timezone.now():
            return False

        self.user = self.email_verify_token.user
        return True
