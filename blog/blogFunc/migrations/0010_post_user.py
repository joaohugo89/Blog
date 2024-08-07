# Generated by Django 5.0.6 on 2024-06-25 01:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogFunc", "0009_post_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
