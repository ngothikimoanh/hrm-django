from django.db import models

from account.validators.user import validate_phone_number


class PhoneNumberField(models.CharField):
    default_validators = [validate_phone_number]
    description = "Phone Number"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 11)
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)

        if value:
            value = value.replace(" ", "")

        return value
