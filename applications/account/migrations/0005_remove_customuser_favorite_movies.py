# Generated by Django 4.2 on 2023-04-16 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_customuser_favorite_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='favorite_movies',
        ),
    ]
