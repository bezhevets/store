from django.urls import path

from users.views import login, registration, profile, logout

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
]

app_name = "users"
