from django import forms
from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    user: User | None = None

    def clean_email(self):
        email = self.cleaned_data["email"]
        self.user = User.objects.filter(email=email).first()
        if self.user is None:
            raise ValidationError(f"User with {email} not found")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if self.user is not None and self.user.check_password(password) is False:
            raise ValidationError("Password is incorrect")
        return password
