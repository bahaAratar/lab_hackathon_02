from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from applications.movie.models import Movie
from .models import CustomUser
from .serializers import *

# User = get_user_model()

class AccountModelViewset(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        user = self.get_object()
        print(f'\n{request}\n')
        movie = Movie.objects.get(id=pk)
        user.favorite_movies.add(movie)
        return Response({'status': 'Movie added to favorites'})

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = self.get_object()
        movie = Movie.objects.get(id=pk)
        user.likes_movies.add(movie)
        return Response({'status': 'Movie liked'})
    

# class FavoriteAPIView(APIView):
#     def get(self, request):
#         # permission_classes = [IsAuthenticatedOrReadOnly]    
#         user = Movie.objects.get()
#         serializer = FavoritSerializer(user)
#         return Response(serializer.data)
    
# class LikeAPIView(APIView):
#     def get(self, request, pk):
#         # permission_classes = [IsAuthenticatedOrReadOnly]    
#         movie = Movie.objects.get(id=pk)
#         serializer = LikeSerializer(movie)
#         return Response(serializer.data)


class RegisterAPIView(APIView):
    
    def post(self, request):
        data = {}
        for i in request.data:
            data.update({i:request.data[i]})
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались', status=201)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        email = request.user.email
        user = authenticate(email=email, password=old_password)

        if user is not None:
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password updated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        secret_word = request.data.get('secret_word')
        new_password = request.data.get('new_password')
        try:
            user = CustomUser.objects.get(email=email, sekret_word=secret_word)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user.password = make_password(new_password)
        user.save()
        return Response({'message': 'Password reset successfully'})
    

