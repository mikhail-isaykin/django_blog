from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseNotAllowed


def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def post_create(request):
    if (
        request.method == "POST"
    ):
        form = PostForm(
            request.POST
        )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(
                "post_list"
            )
        else:
            error = "Форма заполнена неверно"
            return render(
                request, "posts/post_create.html", {"form": form, "error": error}
            )
    else:
        form = PostForm()
        return render(request, "posts/post_create.html", {"form": form})


def post_delete(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return redirect("post_list")
    return HttpResponseNotAllowed(["POST"])
