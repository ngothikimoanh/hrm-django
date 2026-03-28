from abc import ABC, abstractmethod
from datetime import timedelta

from django.conf import settings
from django.utils import timezone


class EmailVerify(ABC):
    def __init__(self):
        self.user = None
        self.token = None

    @abstractmethod
    def clean_data(self, request):
        pass

    @abstractmethod
    def is_valid(self):
        pass

    def is_expired(self, created_at):
        expire_time = created_at + timedelta(minutes=settings.EXPIRY_MINUTES)
        return timezone.now() > expire_time

    def verify(self):
        if not self.token:
            raise Exception("Token not validated")

        if self.is_expired(self.token.created_at):
            raise Exception("Token expired")

        if self.user and not self.user.email_verified:
            self.user.email_verified = True
            self.user.save(update_fields=["email_verified"])
