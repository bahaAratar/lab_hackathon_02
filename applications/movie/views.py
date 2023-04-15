from django.shortcuts import render
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .service import MovieFilter
from .models import *
from .serializers import *

class MovieAPIView(APIView):
    
    def get(self, request):
        # permission_classes = [IsAuthenticatedOrReadOnly]    
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    
class MovieDetailAPIView(APIView):

    def get(self, request, pk):
        # permission_classes = [IsAuthenticatedOrReadOnly]    
        movie = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

class MovieModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    # filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['title', 'tags__name']
    # filterset_fields = ['year', 'genres']

    search_fields = ['title', 'tags']



class CategoryModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorModelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer