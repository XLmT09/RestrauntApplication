from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    class Meta:
        db_table = "Payment"

    paymentID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    timeOfPayment = models.TimeField(auto_now=True, null=False)
    paymentAmount = models.FloatField(null=False)