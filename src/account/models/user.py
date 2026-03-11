from typing import Any

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models

from common.models import TimestampMixin, UUIDPrimaryMixin


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
    class Gender(models.TextChoices):
        MALE = "male"
        FEMALE = "female"

    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_number_verified = models.BooleanField(default=False)

    gender = models.CharField(max_length=6, choices=Gender, null=True, blank=True, default=Gender.FEMALE)

    birthday = models.DateField(null=True, blank=True)

    address = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Remove some fields
    username = None
    date_joined = None

    objects = UserManager()

    def __str__(self) -> str:
        return f"<User: {self.id}>"

    class Meta:
        db_table = "users"
