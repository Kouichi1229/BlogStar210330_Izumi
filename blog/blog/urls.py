"""URL configuration for the local Izumi Blog."""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("context/", include("context.urls")),
    path("", RedirectView.as_view(url="/context/", permanent=False)),
    path("accounts/", include("django.contrib.auth.urls")),
    path("tinymce/", include("tinymce.urls")),
]
