from django.contrib import admin

from .models import Blog_Posts


@admin.register(Blog_Posts)
class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_time")
    list_filter = ("published_time",)
    search_fields = ("title", "content")
    ordering = ("-published_time", "-pk")
