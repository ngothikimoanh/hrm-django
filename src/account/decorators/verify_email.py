from django.http import HttpRequest,HttpResponseRedirect

from account.models.verify_email import  EmailVerifyToken
from account.services.email.verify_email import LinkVerifyEmail


def send_link_verify_email(view_func):
    def wrapped_view(request: HttpRequest, *args, **kwargs):
        response = view_func(request, *args, **kwargs)

        if isinstance(response, HttpResponseRedirect) and response.user:
            email_verify_token = EmailVerifyToken.objects.create(user=response.user)

            email_service = LinkVerifyEmail()
            html_content = email_service.generate_html({"email_verify_token": email_verify_token}, request=request)
            email_service.send_mail(to_emails=[response.user.email], html_content=html_content)

        return response

    return wrapped_view
