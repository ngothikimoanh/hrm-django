from mail.services.smtp import EmailSMTPService


class LinkVerifyEmail(EmailSMTPService):
    subject: str = "Email Address Verification Request"
    template_name: str = "account/mails/verify_email_link.html"


class OTPVerifyEmail(EmailSMTPService):
    subject: str = "Email Address Verification Request"
    template_name: str = "account/mails/verify_email_otp.html"
