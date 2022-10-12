import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='home'),
    path('post/<int:pk>/', views.blog_post_detail, name='post-detail')
]