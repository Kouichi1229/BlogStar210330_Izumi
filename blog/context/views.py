from django.shortcuts import get_object_or_404, render

from .models import Blog_Posts


def index(request):
    return render(request, "context/index.html")


def aboutme(request):
    return render(request, "context/aboutme.html")


def list(request):
    blog_post = Blog_Posts.objects.all()
    return render(request, "context/list.html", {"blog_post": blog_post})


def detail(request, id):
    blog_post = get_object_or_404(Blog_Posts, pk=id)
    return render(request, "context/detail.html", {"blog_post": blog_post})
