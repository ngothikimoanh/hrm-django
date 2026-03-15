from typing import override

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from account.models.user import User


@admin.register(User)
class AdminManager(admin.ModelAdmin):
    list_display = [
        "email",
        "email_verified",
        "phone_number",
        "phone_number_verified",
        "gender",
        "birthday",
        "address",
        "nick_name",
    ]
    search_fields = ["email", "phone_number", "address", "nick_name"]
    list_filter = ["gender"]

    @override
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        return qs.exclude(is_superuser=True)
