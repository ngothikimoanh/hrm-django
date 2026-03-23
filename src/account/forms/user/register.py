from typing import override

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = User
        fields = ["email", "password"]

    @override
    def save(self):
        user = User.objects.create_user(email=self.cleaned_data["email"], password=self.cleaned_data["password"])
        return user
