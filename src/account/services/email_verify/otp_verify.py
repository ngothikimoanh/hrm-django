import logging
from typing import override

from django.contrib.auth import get_user_model
from django.utils import timezone

from account.models.verify_email import EmailVerifyOTP
from account.services.email_verify.base import EmailVerify

User = get_user_model()

logger = logging.getLogger()


class OTPVerifier(EmailVerify):
    def __init__(self, otp: str | None, user: User):
        self.user = user
        self.otp = otp
        self.email_verify_otp: EmailVerifyOTP | None = None

    @override
    def clean(self):
        pass

    @override
    def is_valid(self) -> bool:
        logger.info("Start valid email OTP [%s]", self.otp)

        self.email_verify_otp = EmailVerifyOTP.objects.filter(otp=self.otp).first()

        if self.email_verify_otp is None:
            logger.error("OTP does not exist")
            return False

        if self.email_verify_otp.expired_at < timezone.now():
            logger.error("OTP is expired")
            return False

        self.user = self.email_verify_otp.user
        return True

    def verify(self) -> bool:
        if not self.email_verify_otp:
            logger.error("OTP not validated before verify")
            return False

        self.email_verify_otp.delete()

        self.user.email_verified = True
        self.user.save()

        return True
