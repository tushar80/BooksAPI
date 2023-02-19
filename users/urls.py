from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserRegister

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', TokenObtainPairView.as_view(), name='user_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
