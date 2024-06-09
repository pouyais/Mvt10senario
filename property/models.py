from django.db import models
from agent.models import Agent




class Category_property(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=0)


    def __str__(self):
        return self.title



class Propertie(models.Model):
    image = models.ImageField(upload_to='property',default='notfound.jpg')
    title = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    category = models.ManyToManyField(Category_property)
    rent = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garages = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)


    # def __str__(self):
    #     return self.title


    