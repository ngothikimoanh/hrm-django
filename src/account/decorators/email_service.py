import uuid
from datetime import timedelta

from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from account.models.mails.verify_email import EmailVerificationToken
from mail.services.templates.verify_email import VerifyEmail


def send_verify_email(view_func):
    def wrapped_view(request: HttpRequest, *args, **kwargs):
        response: HttpResponse = view_func(request, *args, **kwargs)

        if isinstance(response, HttpResponseRedirect):
            token = uuid.uuid4()
            expired_at = timezone.now() + timedelta(minutes=settings.EXPIRY_MINUTES)

            EmailVerificationToken.objects.update_or_create(
                user=request.user,
                defaults={"token": token, "expired_at": expired_at},
            )

            path = reverse("verify-email")
            verify_link = request.build_absolute_uri(path) + f"?token={token}"

            email_service = VerifyEmail()
            html_content = email_service.generate_html(
                {
                    "user": request.user,
                    "verify_link": verify_link,
                    "expiry_minutes": settings.EXPIRY_MINUTES,
                }
            )
            email_service.send_mail(to_emails=[request.user.email], html_content=html_content)

        return response

    return wrapped_view
