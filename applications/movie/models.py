from django.db import models
# from django.contrib.auth import get_user_model
# from django.apps import apps

# CustomUser = apps.get_model('account', 'CustomUser')

# User = get_user_model()

class Category(models.Model):
    name = models.CharField('Категория', max_length=150, unique=True)
    discription = models.TextField('Описание')
    url = models.SlugField(max_length=160, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Genre(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    discription = models.TextField('Описание')
    url = models.SlugField(max_length=160, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'

class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Actor(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    age = models.PositiveSmallIntegerField('Возрвст',default=0)
    discription = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actor/')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Актёры и режисеры'
        verbose_name_plural = 'Актёры и режисеры'

class Movie(models.Model):
    title = models.CharField('Название', max_length=255)
    tags = models.ManyToManyField(Tags, verbose_name="теги", related_name="film_tags")
    year = models.PositiveSmallIntegerField('Год выпуска', default='2023')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie/', null=True, blank=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    ) 
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="film_genres")
    # likes = models.ManyToManyField(User, blank=True, related_name='liked_movies')
    # favorites = models.ManyToManyField(User, blank=True, related_name='favorite_movies')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

