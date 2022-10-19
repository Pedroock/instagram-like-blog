from django.urls import path
from . import views

urlpatterns = [
    path('profile/follow', views.AjaxProfileFollow, name='profile-follow'),
    path('profile/unfollow', views.AjaxProfileUnfollow, name='profile-unfollow'),
    path('post/follow', views.AjaxPostLike, name='post-like'),
    path('post/unfollow', views.AjaxPostUnlike, name='post-unlike'),
    path('post/comment', views.AjaxPostComment, name='post-comment'),
    path('profile/query', views.ProfilesQuery, name='profile-query'),
]