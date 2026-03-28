from django.contrib import messages
from django.shortcuts import redirect

from mail.services.link_verify import LinkVerifier


def verify_email_view(request):
    service = LinkVerifier()

    try:
        token = service.clean_data(request)
        service.is_valid(token)
        service.verify()

        messages.success(request, "Email verified successfully!")

    except Exception:
        messages.error(request, "Something went wrong")

    return redirect("account-user-profile")
