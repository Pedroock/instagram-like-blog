from django.db import models
from PIL import Image
from datetime import date
from users.models import UsersProfile
from django_resized import ResizedImageField

# Create your models here.
class BlogPosts(models.Model):
    profile = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    image = ResizedImageField(size=[500, 1500], upload_to='post_images')
    desc = models.CharField(max_length=255)
    date = models.DateField(default=date.today())

