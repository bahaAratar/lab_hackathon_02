from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    favorite_movies = serializers.SlugRelatedField(slug_field='name', read_only=True)
    likes_movies = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

class FavoritSerializer(serializers.ModelSerializer):
    favorite_movies = serializers.SlugRelatedField(slug_field='name', read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('favorite_movies',)

class LikeSerializer(serializers.ModelSerializer):
    likes_movies = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('likes_movies',)

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Password did not match!!!')

        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
