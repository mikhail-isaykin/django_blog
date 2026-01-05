from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):  # основная форма от которой наследуется моя
    email = forms.EmailField(required=True)  # опционально

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
