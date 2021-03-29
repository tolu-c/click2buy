from django.urls import path
from click2buy.views import order_views as views


urlpatterns = [
    path('/add', views.addOrderItems, name='add-order')
]
