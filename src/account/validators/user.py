import re

from django.forms import ValidationError


def validate_phone_number(phone_number: str) -> None:
    if not re.match(r"^0\d{9}$", phone_number):
        raise ValidationError("Phone NUmber is not valid.")
