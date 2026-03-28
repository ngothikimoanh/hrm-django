import uuid
from typing import override

from django.core.exceptions import ValidationError

from account.models.mails.verify_email import EmailVerificationToken
from mail.services.verify_email import EmailVerify


class LinkVerifier(EmailVerify):
    @override
    def clean_data(self, request):
        token_str = request.GET.get("token")

        if not token_str:
            raise ValidationError("Missing token")

        try:
            token = uuid.UUID(token_str)
        except ValueError:
            raise ValidationError("Invalid token format")

        return str(token)

    @override
    def is_valid(self, token):

        record = EmailVerificationToken.objects.get(token=token)

        if record.user.email_verified:
            raise ValidationError("Email already verified")
