from django.shortcuts import render
from project.models import Order
from django.contrib.auth.decorators import user_passes_test

# This lambda expression checks if the user is logged in and has the correct permissions
# If the user does not meet requirments they get redirected to login page
@user_passes_test(lambda u: u.groups.filter(name="KitchenStaff").exists())
# This page wil contain a list of all the confirmed customer orders for the kitchen staff
def order(request):
    # Make a querey to get all customer orders which are confirmed sorted from oldest to newest
    cust_orders = Order.objects.filter(status="Confirmed").order_by('timeOfOrder')
    # list of confimred orders are passed to the html page
    return render(request, 'order.html', {'title': 'Kitchen Staff Orders','cust_orders': cust_orders})