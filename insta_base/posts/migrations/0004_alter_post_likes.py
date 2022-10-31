# Generated by Django 4.1.1 on 2022-10-31 18:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='like_post', to=settings.AUTH_USER_MODEL, verbose_name='Лайк'),
        ),
    ]