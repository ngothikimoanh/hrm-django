import re

from django.forms import ValidationError


def validate_phone_number(phone_number: str) -> None:
    if not re.match(r"^0\d{9}$", phone_number):
        raise ValidationError("Phone Number is not valid.")


def validate_address(address: str) -> None:
    if not re.match(r"^[a-zA-Z0-9\s,./-]+$", address):
        raise ValidationError("Invalid characters in address.")
