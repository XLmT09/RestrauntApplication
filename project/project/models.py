from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import datetime


# Create your models here.

class MenuItem(models.Model):
    class Meta:
        db_table = "MenuItem"

    class MenuItemCourse(models.TextChoices):
        STARTER = "Starter"
        MAIN = "Main"
        DESSERT = "Dessert"
        SIDE = "Side"
        DRINK = "Drink"

    class MenuItemRequirements(models.TextChoices):
        NONE = "None"
        VEGAN = "Vegan"
        VEGETARIAN = "Vegetarian"

    name = models.CharField(max_length=30, primary_key=True)
    price = models.FloatField(null=True)
    calories = models.IntegerField(null=True)
    ingredients = ArrayField(models.TextField())
    alergies = ArrayField(models.TextField())
    description = models.TextField()
    course = models.CharField(max_length=10,choices=MenuItemCourse.choices, null=False, default="Main")
    dietRequirements = models.CharField(max_length=10,choices=MenuItemRequirements.choices, null=False, default="None")
    ID = models.IntegerField(null=True)
# Table which will store all live orders from customers
class Order(models.Model):
    # Add meta data to the order table
    class Meta:
        # Add custom name for the the table
        db_table = "Order"

    # Possible status choices during an customer order

    class orderStatuses(models.TextChoices):
        PLACED = "Placed"
        CONFIRMED = "Confirmed"
        PREPARED = "Prepared"
        DELIVERED = "Delivered"

    ID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    # A feild which should contain one of three status choices
    status = models.CharField(max_length=10, choices=orderStatuses.choices, null=False, default="Placed")
    # Will automatically get the current time due to the auto_now attrbuite
    timeOfOrder = models.TimeField(auto_now=True, null=False)
    orderedItems = ArrayField(models.IntegerField(), null=True)

    

    
