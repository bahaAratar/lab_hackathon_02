# Generated by Django 4.2 on 2023-04-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_category_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='url',
            field=models.SlugField(blank=True, max_length=160),
        ),
    ]
