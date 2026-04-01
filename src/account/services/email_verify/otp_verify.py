import logging
from typing import override

from django.utils import timezone

from account.models.verify_email import EmailVerifyOTP
from account.services.email_verify.base import EmailVerify
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger()


class OTPVerifier(EmailVerify):
    def __init__(self, otp: str| None, user: User):
        self.user = user
        self.otp = otp
        self.email_verify_otp: EmailVerifyOTP | None = None

    @override
    def clean(self):
        pass

    @override
    def is_valid(self) -> bool:
        logger.info("Start valid email otp [%s]", self.otp)
        self.email_verify_otp = EmailVerifyOTP.objects.filter(user=self.user,otp=self.otp).first()

        if self.email_verify_otp is None:
            logger.error("Otp does not exist")
            return False

        if self.email_verify_otp.expired_at < timezone.now():
            logger.error("Otp is expired")
            return False

        self.user = self.email_verify_otp.user
        return True
