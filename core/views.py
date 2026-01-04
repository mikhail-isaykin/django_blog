from django.shortcuts import render
from posts.models import Post


def home(request):
    posts = Post.objects.order_by("-updated_at")[:5]
    return render(request, "core/home.html", {"posts": posts})
