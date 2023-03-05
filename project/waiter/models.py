from django.db import models
from django.contrib.auth.models import User
from project.models import Order

class Payment(models.Model):
    class Meta:
        db_table = "Payment"

    paymentID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    timeOfPayment = models.TimeField(auto_now=True, null=False)
    paymentAmount = models.FloatField(null=False)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE,null=False)

# This table represents the table an waiter will be assigned to in the restraunt
class TableServer(models.Model):
    class Meta:
        db_table = "TableServer"

    tableID = models.AutoField(primary_key=True)
    # OrderID used to grab info about order information such as the customer corrosponding to the order
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    waiterID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)