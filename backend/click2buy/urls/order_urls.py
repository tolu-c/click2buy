from django.urls import path
from click2buy.views import order_views as views


urlpatterns = [
    path('add/', views.addOrderItems, name='add-order'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay', views.updateOrderToPaid, name='pay'),
]
