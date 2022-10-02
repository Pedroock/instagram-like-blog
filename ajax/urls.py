from django.urls import path
from . import views

urlpatterns = [
    path('profile/follow', views.AjaxProfileFollow, name='profile-follow'),
    path('profile/unfollow', views.AjaxProfileUnfollow, name='profile-unfollow'),
]