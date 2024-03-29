# Generated by Django 4.2.7 on 2023-11-21 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog_images/'),
            preserve_default=False,
        ),
    ]
