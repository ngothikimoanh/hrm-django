from http import HTTPMethod

from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.user import require_login
from account.forms.user.change_password import ChangePasswordForm
from account.mail.change_password import ChangePasswordEmail


@require_login
def change_password_view(request: HttpRequest):
    user = request.user
    form = ChangePasswordForm(user, request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()

        ChangePasswordEmail().send(user)

        return redirect("account-user-login")

    return render(request, "account/pages/user/change_password.html", {"form": form})
