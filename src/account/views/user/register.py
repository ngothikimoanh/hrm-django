from http import HTTPMethod

from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.email_service import send_verify_email
from account.decorators.user import require_not_login
from account.forms.user.register import UserRegisterForm


@require_not_login
@send_verify_email
def user_register(request: HttpRequest):
    form = UserRegisterForm(request.POST or None)
    if request.method == HTTPMethod.POST and form.is_valid():
        user = form.save()
        login(request, user)

        response = redirect("account-home")
        setattr(response, "user", user)
        return response

    return render(request, "account/pages/user/register.html", {"form": form})
