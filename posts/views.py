from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def post_create(request):
    """
    1. Пользователь заходит на страницу → метод запроса GET → блок if request.method == 'POST' не выполняется → срабатывает else → создаётся пустая форма → вызывается render() → браузер получает HTML с пустой формой.

    2. Пользователь заполняет форму и нажимает кнопку Submit → браузер отправляет POST-запрос на тот же URL.

    3. Запрос снова попадает в ту же функцию view → теперь request.method == 'POST' → выполняется блок if → данные формы берутся из request.POST, проверяются через form.is_valid() → либо сохраняются и делается redirect, либо возвращается шаблон с формой и ошибкой.
    """
    if (
        request.method == "POST"
    ):  # если POST/если пользователь ввел данный(опционально) и нажал кнопку отправить.../повторный запрос/блок всегда срабатывает вторым
        form = PostForm(
            request.POST
        )  # тогда проверь корректность введенных данных, за эталон возьми описание полей модели
        if form.is_valid():  # валидация ввденных пользователем данных
            post = form.save(commit=False)  # не сохраняем сразу
            post.author = request.user  # добавляем автора
            post.save()  # сохранение нового поста в базу данных
            return redirect(
                "post_list"
            )  # отправь пользователя на url, который в urls.py имеет name='post_list'
        else:
            error = "Форма заполнена неверно"
            return render(
                request, "posts/post_create.html", {"form": form, "error": error}
            )  # оставляем неверно введенные данные, даже если они не прошли валидацию, что бы пользователь их просто отредактировал, и выводим ошибку
    else:  # опционально/если GET/блок всегда срабатывает первым
        form = PostForm()  # пустая форма
        return render(request, "posts/post_create.html", {"form": form})
    
    def post_delete(request):
        pass
