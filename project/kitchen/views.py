from django.shortcuts import render
from project.models import Order
from decerators import group_required
from django.contrib import messages
from django.utils.timezone import localdate

# This page wil contain a list of all the confirmed customer orders for the kitchen staff
@group_required("KitchenStaff")
def order(request):
    if "orderID" in request.COOKIES:
        # Retrieve cookie data
        orderID = request.COOKIES.get("orderID")
        # Retrieve an order object from the database with a given orderID
        order = Order.objects.get(ID = orderID)
        # Set the "status" attribute to prepared for this order
        setattr(order, "status", "Prepared")
        # save the changes to the database
        order.save()
        messages.info(request, f"The order (#{orderID}) has been made by a member of the kitchen staff.")
        # Retrieve the associated customer for the given order
        customer_id = order.customerID
        messages.success(request, f"Message confirming this order has been sent to {customer_id}.")

    currentDate = localdate()
    # Make a querey to get all customer orders which are confirmed sorted from oldest to newest
    cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status="Confirmed", dateOfOrder = currentDate)

    # list of confimred orders are passed to the html page
    return render(request, 'order.html', {'title': 'Kitchen Staff Orders','cust_orders': cust_orders, 'noOfOrders':len(cust_orders)})