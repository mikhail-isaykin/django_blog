from django.shortcuts import render, redirect
from django.contrib.auth import logout
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
        else:
            error = "Форма заполнена неверно"
            return render(
                request, "accounts/register.html", {"form": form, "error": error}
            )
    else:  # опционально/если GET/блок всегда срабатывает первым
        form = RegisterForm()  # пустая форма
        return render(request, "accounts/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('register')
