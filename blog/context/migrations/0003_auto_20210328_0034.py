# Generated by Django 2.2.6 on 2021-03-27 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0002_auto_20210328_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_posts',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 0, 34, 3, 906016), verbose_name='date published'),
        ),
    ]
