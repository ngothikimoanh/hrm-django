from mail.services.smtp import EmailSMTPService

EmailBaseClass = EmailSMTPService


class ChangePasswordEmail(EmailBaseClass):
    subject: str = "Password Changed Successfully"
    template_name: str = "account/mails/change_password.html"
