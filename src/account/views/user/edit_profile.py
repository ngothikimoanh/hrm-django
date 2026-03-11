from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.forms.user.profile import EditProfileGenderForm, EditProfileNameForm

User = get_user_model()


def edit_name_view(request: HttpRequest):
    # lấy user đang login
    user = request.user
    form = EditProfileNameForm(request.POST or None, instance=user)
    if request.method == "POST" and form.is_valid():
        print(form.is_valid())
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_name.html", {"form": form})


def edit_gender_view(request: HttpRequest):
    user = request.user
    form = EditProfileGenderForm(request.POST or None, instance=user)
    if request.method == "POST" and form.is_valid():
        print(form.is_valid())
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_gender.html", {"form": form})


def edit_phone_number_view(request: HttpRequest):
    user = request.user
    form = EditProfileGenderForm(request.POST or None, instance=user)
    if request.method == "POST" and form.is_valid():
        print(form.is_valid())
        form.save()
        return redirect("account-user-profile")
    return render(request, "account/pages/user/profile/edit_phone_number.html", {"form": form})
