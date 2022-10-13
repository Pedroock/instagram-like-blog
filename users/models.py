from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_resized import ResizedImageField
# Create your models here.

class UsersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pfp = ResizedImageField(size=[1920, 1080], upload_to='profile_pics', default='default_pfp.png')
    name = models.CharField(max_length=25)
    bio = models.CharField(max_length=255)
    

class UsersFollowers(models.Model):
    follower = models.ForeignKey(UsersProfile, on_delete=models.CASCADE, related_name='follwer')
    followed = models.ForeignKey(UsersProfile, on_delete=models.CASCADE, related_name='followed')

    def __str__(self):
        return f'{self.follower} follows {self.followed}'
    
