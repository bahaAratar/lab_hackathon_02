# Generated by Django 4.2 on 2023-04-16 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_genre_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='likes',
        ),
    ]