from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', MovieModelViewSet)

urlpatterns = [
    path('all/', MovieAPIView.as_view()),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view()),
    path('favorite/', MovieModelViewSet.as_view({'get': 'favorite'}), name='movie-favorites'),
    path('', include(router.urls))
]