from django.db import models



class Category_new(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class New(models.Model):
    image = models.ImageField(upload_to='blog',default='notfound.jpg')
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.ManyToManyField(Category_new)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title
