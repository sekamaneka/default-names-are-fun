from django.db import models
#we got a class for the supermarkets
#which has a list of products

class Supermarket(models.Model):
    super_name = models.CharField(max_length = 100)
    opening_hours = models.CharField(max_length = 100)

    def __str__(self):
        return self.super_name

class Item(models.Model):
    supermarket = models.ForeignKey(Supermarket)
    i_name = models.CharField(max_length = 100)
    menge = models.CharField(max_length = 100)
    aktion_price = models.CharField(max_length = 30, default = '')
    normal_price = models.CharField(max_length = 30, default = '')
    aktion_grundpreis = models.CharField(max_length = 30, default = '')
    category = models.CharField(max_length = 20, default='')
    aktion = models.CharField(max_length = 20, default = '')

    def __str__(self):
        return self.i_name
    
# Create your models here.
