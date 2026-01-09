from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:  # если пользователь уже зарегистрирован
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:  # опционально/если GET/блок всегда срабатывает первым
        form = RegisterForm()  # пустая форма
        return render(request, "accounts/register.html", {"form": form})
