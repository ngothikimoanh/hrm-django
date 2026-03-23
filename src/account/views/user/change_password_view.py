from http import HTTPMethod

from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.password_success import send_mail_password_success
from account.decorators.user import require_login
from account.forms.user.change_password import ChangePasswordForm


@require_login
@send_mail_password_success
def change_password_view(request: HttpRequest):
    form = ChangePasswordForm(request.user, request.POST or None)

    if request.method == HTTPMethod.POST and form.is_valid():
        form.save()
        return redirect("account-user-login")

    return render(request, "account/pages/user/change_password.html", {"form": form})
