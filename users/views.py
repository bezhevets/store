from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, EmailVerification


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


class EmailVerificationView(TitleMixin, TemplateView):
    title = "Подтверждение email"
    template_name = "user/email_verification.html"
    
    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        user = User.objects.get(email=kwargs["email"])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("products:index"))
