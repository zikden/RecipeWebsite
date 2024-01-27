from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from User.forms import UserLoginForm, UserRegistrationForm


@login_required
def profile(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Твой профиль", "form": form}
    return render(request, "User/profile.html", context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Регистрация", "form": form}
    return render(request, "User/registration.html", context=context)


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()

    context = {"title": "Авторизация", "form": form}
    return render(request, "User/login.html", context=context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("index"))


def password_reset(request):
    context = {
        "title": "Востановление пароля",
    }
    return render(request, "User/password_reset.html", context=context)