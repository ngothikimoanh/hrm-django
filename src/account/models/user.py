from typing import Any

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models

from account.validators.user import validate_address
from common.models import TimestampMixin, UUIDPrimaryMixin
from common.models.fields import PhoneNumberField


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


def upload_avatar(instance, filename):
    ext = filename.split(".")[-1]
    return f"avatars/avatar_{instance.id}.{ext}"


class User(AbstractUser, TimestampMixin, UUIDPrimaryMixin):
    class Gender(models.TextChoices):
        MALE = "male"
        FEMALE = "female"

    avatar = models.ImageField(upload_to=upload_avatar, blank=True, null=True)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)

    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    phone_number_verified = models.BooleanField(default=False)

    gender = models.CharField(max_length=6, choices=Gender, null=True, default=Gender.FEMALE)

    birthday = models.DateField(null=True, blank=True)

    address = models.CharField(max_length=255, validators=[validate_address], blank=True, null=True)

    mid_name = models.CharField(max_length=255, blank=True, null=True)
    nick_name = models.CharField(max_length=255, blank=True, null=True)

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
