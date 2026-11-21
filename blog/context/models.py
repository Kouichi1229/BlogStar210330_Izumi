from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Blog_Posts(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    published_time = models.DateTimeField(
        "date published",
        default=timezone.now,
    )

    class Meta:
        ordering = ["-published_time", "-pk"]
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title
