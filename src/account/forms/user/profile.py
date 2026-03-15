from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditNameForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    mid_name = forms.CharField()
    nick_name = forms.CharField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "mid_name", "nick_name"]


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

        birthday = self.cleaned_data["birthday"]
        return birthday


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["address"]
