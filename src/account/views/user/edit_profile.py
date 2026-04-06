from http import HTTPMethod

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.user import require_login
from account.forms.user.profile import (
    EditAddressForm,
    EditAvatarForm,
    EditBirthdayForm,
    EditEmailForm,
    EditGenderForm,
    EditNameForm,
    EditPhoneNumberForm,
)

User = get_user_model()


@require_login
def edit_avatar_view(request: HttpRequest):
    form = EditAvatarForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        messages.success(request, "Update avatar successfully")
        return redirect("account-user-profile")

    return render(request, "account/pages/user/profile/edit_avatar.html", {"form": form})


@require_login
def edit_name_view(request: HttpRequest):
    form = EditNameForm(request.POST or None, instance=request.user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_name.html", {"form": form})


@require_login
def edit_gender_view(request: HttpRequest):
    form = EditGenderForm(request.POST or None, instance=request.user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_gender.html", {"form": form})


@require_login
def edit_phone_number_view(request: HttpRequest):
    user = request.user
    form = EditPhoneNumberForm(request.POST or None, instance=user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-profile")

    context = {
        "form": form,
        "phone_number_verified": user.phone_number_verified,
    }
    return render(request, "account/pages/user/profile/edit_phone_number.html", context)


@require_login
def edit_email_view(request: HttpRequest):
    user = request.user
    form = EditEmailForm(request.POST or None, instance=user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-profile")
    context = {
        "form": form,
        "email_verified": user.email_verified,
    }

    return render(request, "account/pages/user/profile/edit_email.html", context)


@require_login
def edit_birthday_view(request: HttpRequest):
    form = EditBirthdayForm(request.POST or None, instance=request.user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_birthday.html", {"form": form})


@require_login
def edit_address_view(request: HttpRequest):
    form = EditAddressForm(request.POST or None, instance=request.user)
    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_address.html", {"form": form})
