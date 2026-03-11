from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditProfileNameForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class EditProfileGenderForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["gender"]


class EditPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone_number"]
