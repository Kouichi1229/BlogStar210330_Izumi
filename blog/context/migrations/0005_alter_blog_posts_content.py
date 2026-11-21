# Generated for the Django 5.2 local restoration.
import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("context", "0004_alter_blog_posts_published_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog_posts",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]
