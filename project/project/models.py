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
        VEGAN = "Vegan"
        VEGETARIAN = "Vegetarian"

    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    calories = models.IntegerField()
    cuisine = models.CharField(max_length=10, null=True)
    ingredients = ArrayField(models.TextField())

    course = models.CharField(max_length=10,choices=MenuItemCourse.choices, null=False, default="Main")
    dietRequirements = models.BooleanField(max_length=10,choices=MenuItemRequirements.choices, null=True)
    

# Table which will store all live orders from customers
class Order(models.Model):
    # Add meta data to the order table
    class Meta:
        # Add custom name for the the table
        db_table = "Order"

    # Possible status choices during an customer order
    PLACED = 'PL'
    CONFIRMED = 'CO'
    DELIVERED = 'DE'
    
    STATUS_CHOICES = [
        (PLACED, 'Placed'),
        (CONFIRMED, 'Confirmed'),
        (DELIVERED, 'Delivered'),
    ]

    ID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    # A feild which should contain one of three status choices
    status = models.CharField(max_length=2,choices=STATUS_CHOICES)
    # Will automatically get the current time due to the auto_now attrbuite
    timeOfOrder = models.TimeField(auto_now=True)
    orderedItems = ArrayField(models.IntegerField(), null=True)

    

    
