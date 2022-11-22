from django.db import models

# Create your models here.

class Details(models.Model):
    firstName = models.CharField(max_length = 15)
    secondName = models.CharField(max_length = 15)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    address = models.CharField(max_length = 200)
    productName = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()



