from django.shortcuts import render
from project.models import Order

def order(request):
    cust_orders = Order.objects.filter(status="Confirmed").order_by('timeOfOrder')
    return render(request, 'order.html', {'title': 'Kitchen Staff Orders','cust_orders': cust_orders})