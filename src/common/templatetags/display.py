from datetime import date
from typing import Any

from django.template.defaulttags import register


@register.filter
def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    return str(value)
