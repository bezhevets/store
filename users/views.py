from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

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


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "title": "Store - Профиль",
        "form": form,
        "basket": Basket.objects.filter(user=request.user),
    }
    return render(request, "user/user_profile.html", context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("products:index"))
