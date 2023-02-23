from django.shortcuts import render
from project.models import Order
from decerators import group_required
from django.contrib import messages

# This page wil contain a list of all the confirmed customer orders for the kitchen staff
@group_required("KitchenStaff")
def order(request):
    if "orderID" in request.COOKIES:
        orderID = request.COOKIES.get("orderID")
        order = Order.objects.get(ID = orderID)

        setattr(order, "status", "Prepared")
        order.save()

        messages.info(request, f"The order (#{orderID}) has been made by a member of the kitchen staff.")

        customer_id = order.customerID
        messages.success(request, f"Message confirming this order has been sent to {customer_id}.")


    # Make a querey to get all customer orders which are confirmed sorted from oldest to newest
    cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status="Confirmed")

    # list of confimred orders are passed to the html page
    return render(request, 'order.html', {'title': 'Kitchen Staff Orders','cust_orders': cust_orders})