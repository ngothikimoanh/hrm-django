from django.urls import path

from account.views.home import home_view
from account.views.user.login import user_login
from account.views.user.profile import profile_view
from account.views.user.register import user_register

urlpatterns = [
    path("", home_view, name="account-home"),
    # Users
    path("users/register", user_register, name="account-user-register"),
    path("users/login", user_login, name="account-user-login"),
    path("users/profile", profile_view, name="account-user-profile"),
]
