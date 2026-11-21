# Generated for the Django 5.2 local restoration.
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("context", "0003_auto_20210328_0034"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog_posts",
            name="published_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="date published",
            ),
        ),
    ]
