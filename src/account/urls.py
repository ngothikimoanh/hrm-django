from django.urls import path

from account.views.home import home_view
from account.views.user.edit_profile import edit_gender_view, edit_name_view, edit_phone_number_view
from account.views.user.login import user_login
from account.views.user.profile import profile_view
from account.views.user.register import user_register

urlpatterns = [
    path("", home_view, name="account-home"),
    # Users
    path("users/register", user_register, name="account-user-register"),
    path("users/login", user_login, name="account-user-login"),
    path("users/profile", profile_view, name="account-user-profile"),
    # Edit profile
    path("users/profile/edit_name", edit_name_view, name="account-user-profile-edit-name"),
    path("users/profile/edit_gender", edit_gender_view, name="account-user-profile-edit-gender"),
    path("users/profile/edit_phone_number", edit_phone_number_view, name="account-user-profile-edit-phone_number"),
]
