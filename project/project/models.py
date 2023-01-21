from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    customerID = models.IntegerField() #link to User table as foreign key
    status = models.CharField(max_length=10,choices=orderStatus.choices) #add enums for status
    timeOfOrder = models.TimeField()
    orderedItems = ArrayField(models.IntegerField(), null=True)

    

    
