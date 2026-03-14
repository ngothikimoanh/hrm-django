from django.http import HttpRequest
from django.shortcuts import render

from account.decorators.user import require_login


@require_login
def profile_view(request: HttpRequest):

    return render(
        request,
        "account/pages/user/profile.html",
    )
