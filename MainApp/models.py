from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100,default="")
    count = models.PositiveIntegerField()
    description = models.TextField(max_length=400,default="Описание товара")