from django.db import models

# Create your models here.

class MenuItem(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    calories = models.IntegerField()
    ingredients = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "MenuItem"
