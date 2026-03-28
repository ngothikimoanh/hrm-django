from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from account.services.email.change_password import ChangePasswordEmail


def send_mail_password_success(view_func):
    def wrapped_view(request: HttpRequest, *args, **kwargs):
        response: HttpResponse = view_func(request, *args, **kwargs)

        if isinstance(response, HttpResponseRedirect):
            email_service = ChangePasswordEmail()
            html_content = email_service.generate_html({"user": request.user})
            email_service.send_mail(to_emails=[request.user.email], html_content=html_content)

        return response

    return wrapped_view
