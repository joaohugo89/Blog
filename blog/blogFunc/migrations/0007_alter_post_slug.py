# Generated by Django 5.0.6 on 2024-06-24 01:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogFunc", "0006_remove_post_posts_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title"),
        ),
    ]
