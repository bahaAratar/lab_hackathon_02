from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'category')

class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieFilterSerializer(serializers.ModelSerializer):
    genre = serializers.IntegerField(required=False)
    year = serializers.IntegerField(required=False)

    class Meta:
        model = Movie
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        print(f'\n{obj.favorites.filter(id=user.id).exists()}\n')
        return obj.favorites.filter(id=user.id).exists()