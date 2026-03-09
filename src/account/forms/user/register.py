from typing import Any, override

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

    @override
    def save(self, commit: bool = True) -> Any:
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        return User.objects.create_user(email=email, password=password)
