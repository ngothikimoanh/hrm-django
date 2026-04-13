from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect, render

from account.models.verify_email import EmailVerifyOTP
from account.services.email.verify_email import OTPVerifyEmail
from account.services.email_verify.otp_verify import OTPVerifier

User = get_user_model()


# @require_GET
# def verify_link_email_view(request: HttpRequest):
#     service = LinkVerifier(token=request.GET["token"])
#     service.clean()

#     if service.is_valid():
#         service.save()
#         messages.success(request, "Email verified successfully!")
#         return redirect("account-home")

#     return HttpResponseBadRequest("Invalid token")


def send_otp_view(request: HttpRequest):
    email_verify_otp = EmailVerifyOTP.objects.create(user=request.user)
    email_service = OTPVerifyEmail()
    html_content = email_service.generate_html({"email_verify_otp": email_verify_otp}, request=request)
    email_service.send_mail(to_emails=[request.user.email], html_content=html_content)

    return render(request, "account/otp_verify.html")


def verify_otp_email_view(request: HttpRequest):
    service = OTPVerifier(user=request.user, otp=request.POST.get("otp"))

    try:
        service.clean()
    except ValueError as e:
        return HttpResponseBadRequest(str(e))

    if not service.is_valid():
        return HttpResponseBadRequest("OTP invalid")

    if not service.verify():
        return HttpResponseBadRequest("Verify fail")

    messages.success(request, "Email verified successfully!")
    return redirect("account-home")
