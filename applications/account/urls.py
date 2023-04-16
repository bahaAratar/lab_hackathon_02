from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', AccountModelViewset)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('change-password/', ChangePasswordAPIView.as_view()),
    path('reset-password/', ResetPasswordAPIView.as_view()),

    path('favorite/', FavoriteAPIView.as_view()),
    
    path('', include(router.urls)),
]