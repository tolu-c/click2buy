from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns = [
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoute, name='routes'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
]
