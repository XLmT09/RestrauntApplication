from django.shortcuts import render
from project.models import Order

# This page wil contain a list of all the confirmed customer orders for the kitchen staff
def order(request):
    # Make a querey to get all customer orders which are confirmed sorted from oldest to newest
    cust_orders = Order.objects.filter(status="Confirmed").order_by('timeOfOrder')
    # list of confimred orders are passed to the html page
    return render(request, 'order.html', {'title': 'Kitchen Staff Orders','cust_orders': cust_orders})