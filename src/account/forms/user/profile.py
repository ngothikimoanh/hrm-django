from datetime import date

from django import forms
from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


class EditNameForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class EditGenderForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["gender"]


class EditPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone_number"]


class EditEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        return email


class EditBirthdayForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["birthday"]

    def clean_birthday(self):

        birthday = self.cleaned_data.get("birthday")
        if birthday:
            today = date.today()
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

            if age < 18:
                raise ValidationError("You must be at least 18 years old to use this service.")
        return birthday


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["address"]
