# users/urls.py

from django.conf.urls import url, include
from users.views import dashboard, register

urlpatterns = [
    url("accounts/", include("django.contrib.auth.urls")),
    url("dashboard/", dashboard, name="dashboard"),
    url("oauth/",include("social_django.urls")),
    url("register/",register, name="register"),
]