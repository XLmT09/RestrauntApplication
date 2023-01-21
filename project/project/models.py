from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from account import forms

# Create your models here.

class MenuItem(models.Model):
    class Meta:
        db_table = "MenuItem"

    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    calories = models.IntegerField()
    cuisine = models.CharField(max_length=10, null=True)
    ingredients = ArrayField(models.TextField())
    

class Order(models.Model):
    class Meta:
        db_table = "Order"

    class orderStatus(models.TextChoices):
        PLACED = "Placed"
        CONFIRMED = "Confirmed"
        DELIVERED = "Delivered"

    ID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=orderStatus.choices)
    timeOfOrder = models.TimeField()
    orderedItems = ArrayField(models.IntegerField(), null=True)

    

    
