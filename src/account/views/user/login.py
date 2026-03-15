from http import HTTPMethod

from django.contrib.auth import get_user_model, login
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.forms.user.login import UserLoginForm

User = get_user_model()


def user_login(request: HttpRequest):
    form = UserLoginForm(request.POST or None)
    if request.method == HTTPMethod.POST and form.is_valid() and form.user is not None:
        login(request, user=form.user)
        return redirect("account-home")
    return render(request, "account/pages/user/login.html", {"form": form})
