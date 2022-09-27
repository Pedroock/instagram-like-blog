from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.users_register, name='register'),
    path('logout/', views.users_logout, name='logout'),
    path('login/', views.users_login, name='login'),
    path('profile/<int:pk>', views.users_profile, name='profile'),   
    path('profile/<int:pk>/update', views.users_profile_update, name='profile-update'),                    
]