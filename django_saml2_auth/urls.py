from django.urls import include, re_path, path
from . import views

app_name = "django_saml2_auth"

urlpatterns = [
    path("acs/", views.acs, name="acs"),
    path("welcome/", views.welcome, name="welcome"),
    path("denied/", views.denied, name="denied"),
    path("accounts/login/", views.signin, name="login"),
    path("accounts/logout/", views.signout, name="logout"),
]
