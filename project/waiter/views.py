from django.shortcuts import render
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem
from project.models import Order

# Make http requests to the waiter page
def staff(request):
    return render(request, "staffPage.html", {'title' : 'staff'})

# Make http requests on page that gives list of customer orders
def viewOrders(request):
    # retrive all customer orders from oldest to newest
    cust_orders = Order.objects.all().order_by('timeOfOrder')
    return render(request, "orders.html", {'cust_orders': cust_orders})

# Make http requests on page that shows menu and allows modification to the menu
def changeMenu(request):
    if request.method == "POST":
        form = menuUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Menu has been updated successfully')
        else:
            messages.error(request, f'Failed to update menu!')
    else:
        form = menuUpdateForm()

    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all(),"itemToDelete" : None})

def deleteItem(request, itemToDelete): 
    if itemToDelete == None:
        messages.error(request, f'No item selected to delete')
    else:
        MenuItem.objects.filter(name=itemToDelete).delete()
        messages.success(request, f'Item has successfully been deleted') #Message is displayed on the main page when it's not supposed to
    form = menuUpdateForm()
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all(), "itemToDelete" : None})

def refreshMenu(request, item):
    if item == None:
        form = menuUpdateForm()
    else:
        form = menuUpdateForm(instance=MenuItem.objects.get(name=item))
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all(), 'itemToDelete': item})
