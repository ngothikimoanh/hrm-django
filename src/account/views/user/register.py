from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from account.decorators.user import require_not_login
from account.forms.user.register import UserRegisterForm
from account.services.email.verify_email import LinkVerifyEmail
from account.services.user import UserService


@require_not_login
def user_register(request: HttpRequest):
    form = UserRegisterForm(request.POST or None)
    if not form.is_valid():
        return render(request, "account/pages/user/register.html", {"form": form})

    email = form.cleaned_data["email"]
    password = form.cleaned_data["password"]

    user_service = UserService()

    if user_service.get_by_email(email):
        return render(
            request,
            "account/pages/user/register.html",
            {
                "form": form,
                "error": "Email is already exist.",
            },
        )

    if not user_service.has_any_user():
        user = user_service.create_admin(email=email, password=password)
    else:
        user = user_service.create_guest_user(email=email, password=password)

    email_service = LinkVerifyEmail()
    email_verify_token = email_service.create_token(user=user)
    html_content = email_service.generate_html({"email_verify_token": email_verify_token}, request=request)
    email_service.send_mail(to_emails=[user.email], html_content=html_content)

    messages.success(request, "Account created. Please check your email to verify.")
    return redirect("account-home")
