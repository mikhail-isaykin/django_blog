from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # через класс Meta связываем форму и модель Post, для последующей валидации данных
        fields = ["title", "content"]  # поля, которые пользователь будет заполнять
