from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("products:index"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "registration/login.html", context=context)


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user/user_registration.html"
    success_url = reverse_lazy("users:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context["title"] = "Store - Регистрация"
        return context


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "user/user_profile.html"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context["title"] = "Store - Профиль"
        context["basket"] = Basket.objects.filter(user=self.request.user)
        return context


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("products:index"))
