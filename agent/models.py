from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='agent',default='default.jpg')
    title = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    description = models.TextField()
    phone = models.IntegerField(default=0)
    email = models.TextField(null=True)
    facebook = models.CharField(max_length=220,default="#")
    x = models.CharField(max_length=220,default="#")
    instagram = models.CharField(max_length=220,default="#")
    linkedin = models.CharField(max_length=220,default="#")
    status = models.BooleanField(max_length=220,default=True)


    def __str__(self):
        return self.title
