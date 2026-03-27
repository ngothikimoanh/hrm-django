from http import HTTPMethod

from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.email_service import send_verify_email
from account.decorators.user import require_not_login
from account.forms.user.register import UserRegisterForm


@send_verify_email
@require_not_login
def user_register(request: HttpRequest):
    form = UserRegisterForm(request.POST or None)
    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("account-home")
    return render(request, "account/pages/user/register.html", {"form": form})
