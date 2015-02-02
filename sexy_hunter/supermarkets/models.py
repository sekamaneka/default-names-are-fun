from django.db import models
#we got a class for the supermarkets
#which has a list of products

class Supermarket(models.Model):
    super_name = models.CharField(max_length = 30)
    opening_hours = models.CharField(max_length = 100)

    def __str__(self):
        return self.super_name

class Item(models.Model):
    supermarket = models.ForeignKey(Supermarket)
    i_name = models.CharField(max_length = 50)
    price = models.CharField(max_length = 30)
    category = models.CharField(max_length = 20)

    def __str__(self):
        return self.i_name
    
# Create your models here.
