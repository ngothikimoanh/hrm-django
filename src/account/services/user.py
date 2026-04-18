from account.models.user import User


class UserService:
    def has_any_user(self) -> bool:
        return User.objects.exists()

    def get_by_email(self, email: str):
        return User.objects.filter(email=email).first()

    def create_guest_user(self, email: str, password: str, **extra_fields):
        user = User(email=email, **extra_fields)
        user.set_password(raw_password=password)
        user.save()

        return user

    def create_admin(self, email: str, password: str, **extra_fields):
        extra_fields.update(
            {
                "is_active": True,
                "is_staff": True,
                "is_superuser": True,
            }
        )
        return self.create_guest_user(email, password, **extra_fields)
