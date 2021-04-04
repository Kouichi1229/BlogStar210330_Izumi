from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Posts
from .forms import *
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView 


def index(request):
	return render(request,'context/index.html')

def aboutme(request):
	return render(request,'context/aboutme.html')

def list(request):
	blog_post = Blog_Posts.objects.all()

	context ={
		"blog_post":blog_post,
	}
	return render(request,'context/list.html',context)

def detail(request, id):
	blog_post = get_object_or_404(Blog_Posts, pk=id)

	context ={
		"blog_post":blog_post,
	}
	return render(request,'context/detail.html',context)

def delete(request, id):
    blog_post = get_object_or_404(Blog_Posts, pk=id)
    blog_post.delete()

    blog_posts = Blog_Posts.objects.all()
    context = {
        'message': '削除',
        'blog_posts': blog_posts,
    }
    return render(request, 'context/delete.html', context)

def edit(request, id):
    blog_posts = get_object_or_404(Blog_Posts, pk=id)
    blogEditForm = BlogEditForm(instance=blog_posts)

    context = {
        'message': blog_posts.title,
        'blog_posts': blog_posts,
        'blogEditForm': blogEditForm,
    }
    return render(request, 'context/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        blog_post = get_object_or_404(Blog_Posts, pk=id)
        blogEditForm = BlogEditForm(request.POST, instance=blog_post)
        if blogEditForm.is_valid():
            blogEditForm.save()

    context = {
        'message': 'Update memo ' + str(id),
        'blog_post': blog_post,
    }
    return render(request, 'context/show.html', context)

def create(request):
    if request.method == 'POST':
        blogEditForm = BlogEditForm(request.POST)
        if blogEditForm.is_valid():
            blog_post = blogEditForm.save()

    context = {
        'message': 'Create blog_post ',
        'blog_post': blog_post,
    }
    return render(request, 'context/detail.html', context)

def new(request):
    blogEditForm = BlogEditForm()

    context = {
        'message': 'New blog_post',
        'blogEditForm': blogEditForm,
    }
    return render(request, 'context/new.html', context)