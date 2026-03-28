import secrets

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models.timestamp import TimestampMixin

User = get_user_model()


def _generate_exp_time():
    return timezone.now() + settings.EMAIL_VERIFY_EXP


def _generate_secret() -> str:
    return secrets.token_urlsafe(32)


class EmailVerifyToken(TimestampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128, default=_generate_secret)
    expired_at = models.DateTimeField(default=_generate_exp_time)

    class Meta:
        db_table = "email_verify_tokens"
