from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model

User = get_user_model()


class EmailVerify(ABC):
    def __init__(self) -> None:
        self.user: User

    @abstractmethod
    def clean(self): ...

    @abstractmethod
    def is_valid(self) -> bool: ...

    def save(self):
        self.user.email_verified = True
        self.user.save(update_fields=["email_verified"])
