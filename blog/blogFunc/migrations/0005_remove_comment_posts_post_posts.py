# Generated by Django 5.0.6 on 2024-06-24 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogFunc", "0004_comment_posts_alter_category_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="posts",
        ),
        migrations.AddField(
            model_name="post",
            name="posts",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="blogFunc.category",
            ),
            preserve_default=False,
        ),
    ]
