from django.urls import path

from users.views import UserCreateView, UserProfileView, UserLoginView, UserLogoutView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("registration/", UserCreateView.as_view(), name="registration"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
]

app_name = "users"
