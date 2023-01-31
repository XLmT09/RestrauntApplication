from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import Order

# Make http requests to the waiter page
def staff(request):
    return render(request, "staffPage.html", {'title' : 'staff'})

# Make http requests on page that gives list of customer orders
def viewOrders(request):
    # retrive all customer orders from oldest to newest
    cust_orders = Order.objects.all().order_by('timeOfOrder')
    return render(request, "Orders.html", {'cust_orders': cust_orders})

# Make http requests on page that shows menu and allows modification to the menu
def changeMenu(request):
    if request.method == "POST":
        form = menuUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Menu has been updated successfully')
            HttpResponseRedirect("staffPage.html")
    else:
        form = menuUpdateForm()
    
    return render(request, "changeMenu.html", {'form' : form})



