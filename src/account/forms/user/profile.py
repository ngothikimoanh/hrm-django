from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditAvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar"]


class EditNameForm(forms.ModelForm):
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


class EditBirthdayForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["birthday"]


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["address"]
