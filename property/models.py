from django.db import models



class Propertie(models.Model):
    image = models.ImageField(upload_to='property',default='notfound.jpg')
    title = models.CharField(max_length=100)
    rent = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garages = models.IntegerField(default=0)


    