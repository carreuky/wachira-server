# Generated by Django 4.2.7 on 2023-11-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.URLField(max_length=500),
        ),
    ]
