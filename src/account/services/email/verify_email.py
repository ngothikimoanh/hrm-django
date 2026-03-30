from mail.services.smtp import EmailSMTPService


class VerifyEmail(EmailSMTPService):
    subject: str = "Email Address Verification Request"
    template_name: str = "account/mails/verify_email.html"
