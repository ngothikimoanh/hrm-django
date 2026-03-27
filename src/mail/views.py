import uuid

from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.utils import timezone

from mail.models import EmailVerificationToken

User = get_user_model()


def verify_email_view(request):
    token_str = request.GET.get("token")

    if not token_str:
        messages.error(request, "Invalid verification link.")
        return redirect("account-home")

    try:
        token = uuid.UUID(token_str)

    except ValueError:
        messages.error(request, "Invalid verification link.")
        return redirect("account-home")

    try:
        record = EmailVerificationToken.objects.get(token=token)

    except EmailVerificationToken.DoesNotExist:
        messages.error(request, "Verification token not found.")
        return redirect("account-home")

    if record.is_used:
        messages.error(request, "This verification link has already been used.")
        return redirect("account-home")

    if record.expired_at < timezone.now():
        record.delete()
        messages.error(request, "Verification link has expired.")
        return redirect("account-home")

    user = record.user

    user.email_verified = True
    user.save(update_fields=["email_verified"])

    record.is_used = True
    record.save(update_fields=["is_used"])

    auth.login(request, user)

    messages.success(request, f"{user.email}! has been verified successfully!")
    return redirect("account-user-profile")
