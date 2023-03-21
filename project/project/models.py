from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Table which will store all the food menu items 
class MenuItem(models.Model):
    class Meta:
        # customer name for table
        db_table = "MenuItem"

    # Possible menu courses a food can be part of
    class MenuItemCourse(models.TextChoices):
        STARTER = "Starter"
        MAIN = "Main"
        DESSERT = "Dessert"
        SIDE = "Side"
        DRINK = "Drink"

    # Possible menu requirments
    class MenuItemRequirements(models.TextChoices):
        NONE = "None"
        VEGAN = "Vegan"
        VEGETARIAN = "Vegetarian"

    name = models.CharField(max_length=30, primary_key=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    calories = models.IntegerField(null=True)
    alergies = models.TextField()
    description = models.TextField()
    course = models.CharField(max_length=10,choices=MenuItemCourse.choices, null=False, default="Main")
    dietRequirements = models.CharField(max_length=10,choices=MenuItemRequirements.choices, null=False, default="None")
    ID = models.IntegerField(null=True)
    imgurl = models.URLField(default = 'https://i.postimg.cc/PqLn57Cr/No-Image-Available.png')
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
    dateOfOrder = models.DateField(auto_now=True, null=False)
    orderedItems = models.JSONField(null=False)
    notificationSent = models.BooleanField(default=False)

# Table which stores help request messages a customer makes
class HelpRequest(models.Model):
    class Meta:
        db_table = "HelpRequest"

    requestID = models.AutoField(primary_key=True, null = False)
    # Need customerID so staff can locate which customer needs help
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100, null=True)

    
