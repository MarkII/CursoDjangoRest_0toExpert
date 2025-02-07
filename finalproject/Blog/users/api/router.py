from django.urls import path
from users.api.views import RegisterUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""
    TokenObtainPairView -> Para hacer login con token
    TokenFreshView -> Para refrescar el token
"""

urlpatterns = [
    path('auth/register', RegisterUserView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/token/refresh',  TokenRefreshView.as_view()),
]