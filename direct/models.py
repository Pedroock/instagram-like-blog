from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DirectChatMessage(models.Model):
    message = models.CharField(max_length=255)
    chat_id = models.IntegerField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
