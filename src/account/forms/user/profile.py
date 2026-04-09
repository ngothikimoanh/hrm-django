from typing import override

from django import forms
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage

User = get_user_model()


class EditAvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar"]

    @override
    def save(self):
        instance = super().save(commit=False)

        if instance.id:
            try:
                old_instance = User.objects.get(id=instance.id)
                old_avatar = old_instance.avatar
                new_avatar = self.cleaned_data.get("avatar")

                if new_avatar and old_avatar and old_avatar != new_avatar:
                    if default_storage.exists(old_avatar.name):
                        default_storage.delete(old_avatar.name)
            except User.DoesNotExist:
                pass

        instance.save()
        return instance


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
