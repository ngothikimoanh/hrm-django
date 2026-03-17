from http import HTTPMethod

from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.user import require_login
from account.forms.user.change_password import ChangePasswordForm


@require_login
def change_password_view(request: HttpRequest):
    user = request.user
    form = ChangePasswordForm(user, request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        print(form.errors)
        user = form.save()

        logout(request)
        return redirect("account-user-login")

    return render(request, "account/pages/user/change_password.html", {"form": form})
