from django import forms
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("Password is incorrect. Please try again!")

        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data["new_password"]
        validate_password(new_password, self.user)
        return new_password

    def clean(self):
        cleaned_data = super().clean()

        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")

        if new_password and confirm_new_password:
            if self.user.check_password(new_password):
                self.add_error("new_password", "New password must be different from old password.")

            if confirm_new_password and new_password != confirm_new_password:
                self.add_error("confirm_new_password", "Passwords do not match.")

        return cleaned_data

    def save(self):
        user = self.user
        new_password = self.cleaned_data["new_password"]

        user.set_password(new_password)
        user.save()

        return user
