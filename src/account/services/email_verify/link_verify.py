# import logging
# from typing import override

# from django.utils import timezone

# from account.models.verify_email import EmailVerifyToken
# from account.services.email_verify.base import EmailVerify

# logger = logging.getLogger()


# class LinkVerifier(EmailVerify):
#     def __init__(self, token: str):
#         self.token = token
#         self.email_verify_token: EmailVerifyToken | None = None

#     @override
#     def clean(self):
#         pass

#     @override
#     def is_valid(self) -> bool:
#         logger.info("Start valid email token [%s]", self.token)
#         self.email_verify_token = EmailVerifyToken.objects.filter(token=self.token).first()

#         if self.email_verify_token is None:
#             logger.error("Token does not exist")
#             return False

#         if self.email_verify_token.expired_at < timezone.now():
#             logger.error("Token is expired")
#             return False

#         self.user = self.email_verify_token.user
#         return True
