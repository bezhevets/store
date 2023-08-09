from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm



def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            print(password)
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("products:index"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "registration/login.html", context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Поздравляем! Вы успешно зарегестрировались")
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "user/user_registration.html", context=context)

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
