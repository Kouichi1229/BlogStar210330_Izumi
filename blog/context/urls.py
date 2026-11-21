from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("list", views.list, name="list"),
    path("<int:id>", views.detail, name="detail"),
]
