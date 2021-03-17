from django.urls import path
from click2buy.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('profile/', views.getUserProfile, name='user-profile'),
    path('', views.getUsers, name='users'),
    path('<str:pk>/', views.getUserById, name='user'),
    path('register/', views.registerUser, name='register'),
]
