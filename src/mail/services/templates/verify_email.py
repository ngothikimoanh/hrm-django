from mail.services.smtp import EmailSMTPService

EmailBaseClass = EmailSMTPService


class VerifyEmail(EmailBaseClass):
    subject: str = "Email Address Verification Request"
    template_name: str = "account/mails/verify_email.html"
