from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = "registration/login.html"
    form_class = UserLoginForm
    title = "Login"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("products:index")


class UserCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user/user_registration.html"
    success_url = reverse_lazy("users:login")
    success_message = "Поздравляем! Вы успешно зарегестрировались"
    title = "Store - Регистрация"


class UserProfileView(TitleMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "user/user_profile.html"
    title = "Store - Профиль"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context["basket"] = Basket.objects.filter(user=self.request.user)
        return context
