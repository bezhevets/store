from django.urls import path

from users.views import login, registration

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
]

app_name = "users"
