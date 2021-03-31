from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog_Posts
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView 
#from .forms import BlogEditForm


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

