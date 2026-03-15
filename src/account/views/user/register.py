from http import HTTPMethod

from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.forms.user.register import UserRegisterForm


def user_register(request: HttpRequest):
    form = UserRegisterForm(request.POST or None)
    if request.method == HTTPMethod.POST and form.is_valid():
        print(form.is_valid())
        print(form.errors)
        user = form.save()
        login(request, user)
        return redirect("account-home")
    return render(request, "account/pages/user/register.html", {"form": form})
