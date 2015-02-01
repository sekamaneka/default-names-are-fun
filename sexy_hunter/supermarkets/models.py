from django.db import models
#we got a class for the supermarkets
#which has a list of products

class Supermarket(models.Model):
    name = models.CharField(max_length = 30)
    opening_hours = models.CharField(max_length = 100)
    pass


class Item(models.Model):
    supermarket = models.ForeignKey(Supermarket)
    name = models.CharField(max_length = 50)
    price = models.CharField(max_length = 30)
    
# Create your models here.
