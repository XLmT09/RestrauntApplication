from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from account import forms





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

    

    
