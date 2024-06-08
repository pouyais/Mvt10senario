from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='agent',default='default.jpg')
    title = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.IntegerField(default=0)

