# Generated by Django 4.2 on 2023-04-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_remove_movie_favorites_remove_movie_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайки'),
        ),
    ]