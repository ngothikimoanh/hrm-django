from django.contrib import messages
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_GET

from account.services.email_verify.link_verify import LinkVerifier


@require_GET
def verify_email_view(request: HttpRequest):
    service = LinkVerifier(token=request.GET["token"])
    service.clean()

    if service.is_valid():
        service.save()
        messages.success(request, "Email verified successfully!")
        return redirect("account-home")

    return HttpResponseBadRequest("Invalid token")
