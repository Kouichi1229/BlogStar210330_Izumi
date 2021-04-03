from django.urls import path
from . import views
from django.contrib import staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog'

urlpatterns = [    
	path('', views.index, name='index'),
	path('aboutme', views.aboutme, name='aboutme'),
	path('list', views.list, name='list'),
	path('<int:id>', views.detail, name='detail'),
	path('<int:id>/delete', views.delete, name='delete'),
	path('create', views.create, name='create'),
	path('<int:id>/edit', views.edit, name='edit'),
	path('<int:id>/update', views.update, name='update'),
]
urlpatterns += staticfiles_urlpatterns()