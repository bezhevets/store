from django.urls import path

from users.views import login, logout, UserCreateView, UserProfileView

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("logout/", logout, name="logout"),
]

app_name = "users"
