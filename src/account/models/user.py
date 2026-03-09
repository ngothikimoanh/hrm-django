from typing import Any

from common.models import TimestampMixin, UUIDPrimaryMixin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models


class UserManager(AbstractUserManager):
    @classmethod
    def normalize_email(cls, email):
        if email is None:
            return None
        return super().normalize_email(email)

    def create_user(self, email: str, password: str, **extra_fields: Any) -> "User":
        user = self.model(email=email, **extra_fields)
        user.set_password(raw_password=password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Any) -> "User":
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, TimestampMixin, UUIDPrimaryMixin):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_number_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Remove some fields
    username = None
    first_name = None
    last_name = None
    date_joined = None

    objects = UserManager()

    def __str__(self) -> str:
        return f"<User: {self.id}>"

    class Meta:
        db_table = "users"
