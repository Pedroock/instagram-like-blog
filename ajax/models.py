from statistics import mode
from django.db import models
from users.models import UsersProfile, UsersFollowers
from blog.models import BlogPosts, BlogPostsComments, BlogPostsLikes
# Create your models here.

class AjaxNotification(models.Model):
    notifier = models.ForeignKey(UsersProfile, on_delete=models.CASCADE, related_name='notification')
    action = models.CharField(max_length=50)
    post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    like_obj = models.ForeignKey(BlogPostsLikes, on_delete=models.CASCADE, null=True, blank=True)
    comment_obj = models.ForeignKey(BlogPostsComments, on_delete=models.CASCADE, null=True, blank=True)
    follow_obj = models.ForeignKey(UsersFollowers, on_delete=models.CASCADE, null=True, blank=True)