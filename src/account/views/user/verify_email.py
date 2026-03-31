from django.contrib import messages
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_GET,require_POST

from account.models.verify_email import EmailVerifyOTP
from account.services.email.verify_email import OTPVerifyEmail
from account.services.email_verify.link_verify import LinkVerifier

from django.shortcuts import render

from account.services.email_verify.otp_verify import OTPVerifier
from django.contrib.auth import get_user_model

User = get_user_model()


@require_GET
def verify_link_email_view(request: HttpRequest):
    service = LinkVerifier(token=request.GET["token"])
    service.clean()

    if service.is_valid():
        service.save()
        messages.success(request, "Email verified successfully!")
        return redirect("account-home")

    return HttpResponseBadRequest("Invalid token")


def otp_view(request: HttpRequest):
    if request.method != "POST":
        return redirect("otp")

    EmailVerifyOTP.objects.filter(user=request.user).delete()

    email_verify_otp = EmailVerifyOTP.objects.create(user=request.user)
    email_service = OTPVerifyEmail()
    html_content = email_service.generate_html({"email_verify_otp": email_verify_otp}, request=request)
    email_service.send_mail(to_emails=[request.user.email],html_content=html_content)

    return render(request, "account/otp_verify.html")


def verify_otp_email_view(request: HttpRequest):
    service = OTPVerifier(user=request.user, otp=request.POST.get("otp"))
    service.clean()

    if service.is_valid():
        service.save()
        messages.success(request, "Email verified successfully!")
        return redirect("account-home")

    return HttpResponseBadRequest("Invalid token")
