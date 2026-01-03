from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('-updated_at')[:5]
    return render(request, 'posts/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})
