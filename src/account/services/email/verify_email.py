from account.models.verify_email import EmailVerifyOTP, EmailVerifyToken
from mail.services.smtp import EmailSMTPService


class LinkVerifyEmail(EmailSMTPService):
    subject: str = "Email Address Verification Request"
    template_name: str = "account/mails/verify_email_link.html"

    def create_token(self, user):
        return EmailVerifyToken.objects.create(user=user)


class OTPVerifyEmail(EmailSMTPService):
    subject: str = "Email Address Verification Request"
    template_name: str = "account/mails/verify_email_otp.html"

    def create_and_send(self, user, request):

        EmailVerifyOTP.objects.filter(user=user).delete()

        otp = EmailVerifyOTP.objects.create(user=user)

        html_content = self.generate_html({"email_verify_otp": otp}, request=request)

        self.send_mail(to_emails=[user.email], html_content=html_content)

        return otp
