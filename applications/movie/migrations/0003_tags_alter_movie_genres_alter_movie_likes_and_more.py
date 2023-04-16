# Generated by Django 4.2 on 2023-04-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='film_genres', to='movie.genre', verbose_name='жанры'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(blank=True, default=0, verbose_name='Лайки'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tags',
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(related_name='film_tags', to='movie.tags', verbose_name='теги'),
        ),
    ]