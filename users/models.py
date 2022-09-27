from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UsersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pfp = models.ImageField(upload_to='profile_pics', default='default_pfp.png')
    name = models.CharField(max_length=25)
    bio = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        with Image.open(self.pfp) as im:
            width = im.size[0]
            height = im.size[1]
            new_width  = 150
            new_height = int(new_width * height / width) 
            im = im.resize((new_width, new_height), Image.ANTIALIAS)
            im.save(self.pfp.path, format='JPEG', quality=100)
        super(UsersProfile, self).save(*args, **kwargs)