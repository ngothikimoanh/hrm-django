from account.services.email.base import EmailBaseClass


class ChangePasswordEmail(EmailBaseClass):
    subject: str = "Password Changed Successfully"
    template_name: str = "account/mails/change_password.html"
