from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views.home import home_view
from account.views.user.change_password_view import change_password_view
from account.views.user.edit_profile import (
    edit_address_view,
    edit_avatar_view,
    edit_birthday_view,
    edit_email_view,
    edit_gender_view,
    edit_name_view,
    edit_phone_number_view,
)
from account.views.user.login import user_login
from account.views.user.profile import profile_view
from account.views.user.register import user_register
from account.views.user.verify_email import send_otp_view, verify_otp_email_view

urlpatterns = [
    path("", home_view, name="account-home"),
    # Users
    path("users/register", user_register, name="account-user-register"),
    path("users/login", user_login, name="account-user-login"),
    path("users/logout", LogoutView.as_view(next_page="account-home"), name="account-user-logout"),
    path("users/profile", profile_view, name="account-user-profile"),
    path("users/change_password", change_password_view, name="account-user-change_password"),
    # Edit profile
    path("users/profile/edit_avatar", edit_avatar_view, name="account-user-profile-edit-avatar"),
    path("users/profile/edit_name", edit_name_view, name="account-user-profile-edit-name"),
    path("users/profile/edit_gender", edit_gender_view, name="account-user-profile-edit-gender"),
    path("users/profile/edit_phone_number", edit_phone_number_view, name="account-user-profile-edit-phone_number"),
    path("users/profile/edit_email", edit_email_view, name="account-user-profile-edit-email"),
    path("users/profile/edit_birthday", edit_birthday_view, name="account-user-profile-edit-birthday"),
    path("users/profile/edit_address", edit_address_view, name="account-user-profile-edit-address"),
    # send mail
    # path("link_verify_email", verify_link_email_view, name="link-verify-email"),
    path("otp", send_otp_view, name="otp"),
    path("otp_verify_email", verify_otp_email_view, name="otp_verify_email"),
]
