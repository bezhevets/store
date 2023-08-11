from django.urls import path

from users.views import login, profile, logout, UserCreateView

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
]

app_name = "users"
