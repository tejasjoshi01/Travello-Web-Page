from django.db import models

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100, default='Amravati')
    img = models.ImageField(upload_to='pics', default=None)
    desc = models.TextField(default='Very Nice Place Be There!!')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

