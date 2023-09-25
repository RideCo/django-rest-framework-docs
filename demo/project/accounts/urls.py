from django.urls import re_path
from project.accounts import views

app_name = "accounts"

urlpatterns = [
    re_path(r'^test/$', views.TestView.as_view(), name="test-view"),

    re_path(r'^login/$', views.LoginView.as_view(), name="login"),
    re_path(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    re_path(r'^reset-password/$', view=views.PasswordResetView.as_view(), name="reset-password"),
    re_path(r'^reset-password/confirm/$', views.PasswordResetConfirmView.as_view(), name="reset-password-confirm"),

    re_path(r'^user/profile/$', views.UserProfileView.as_view(), name="profile"),

]
