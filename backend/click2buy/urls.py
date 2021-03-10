from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute, name='routes'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
]
