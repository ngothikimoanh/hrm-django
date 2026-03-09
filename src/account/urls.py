from django.urls import path

from account.views.home import home_view
from account.views.user.register import user_register

urlpatterns = [
    path("", home_view, name="account-home"),
    # Users
    path("users/register", user_register, name="account-user-register"),
]
