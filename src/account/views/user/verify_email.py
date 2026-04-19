from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET

from account.models.verify_email import EmailVerifyOTP
from account.services.email.verify_email import OTPVerifyEmail
from account.services.email_verify.link_verify import LinkVerifier
from account.services.email_verify.otp_verify import OTPVerifier

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


def send_otp_view(request: HttpRequest):
    service = OTPVerifyEmail()
    service.create_and_send(request.user, request)
    return render(request, "account/otp_verify.html")


def verify_otp_email_view(request: HttpRequest):
    if request.method != "POST":
        return render(request, "account/otp_verify.html")

    service = OTPVerifier(user=request.user, otp=request.POST.get("otp"))

    try:
        service.clean()
    except ValueError as e:
        messages.error(request, str(e))
        return redirect("otp_verify")

    if not service.is_valid():
        messages.error(request, "OTP invalid")
        return redirect("otp_verify")

    if not service.verify():
        messages.error(request, "Verify failed")
        return redirect("otp_verify")

    messages.success(request, "Email verified successfully!")
    return redirect("account-home")


def resend_otp_view(request):
    user = request.user
    now = timezone.now()

    otp_obj = EmailVerifyOTP.objects.filter(user=user).first()

    if otp_obj and otp_obj.expired_at > now:
        remaining = int((otp_obj.expired_at - now).total_seconds())

        messages.error(request, f"Your current OTP is still valid for {remaining} seconds.")
        return redirect("otp_verify")

    OTPVerifyEmail().create_and_send(user, request)

    messages.success(request, "A new OTP has been sent successfully.")
    return redirect("otp_verify")
