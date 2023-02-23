from django.shortcuts import render
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem
from project.models import Order
from project.models import HelpRequest
from django.shortcuts import redirect

# Make http requests to the waiter page
def staff(request):
    return render(request, "staffPage.html", {'title' : 'staff'})

# Make http requests on page that gives list of customer orders
def viewOrders(request, orderStatus):
    # retrive all customer orders from oldest to newest
    cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status = orderStatus)

    return render(request, "orders.html", {'cust_orders': cust_orders})



def updateOrderStatus(request, orderID):
    order = Order.objects.get(ID = orderID)

    if (order.status == "Placed"):
        setattr(order, "status", "Confirmed")
        filterStatus = "Placed"

    elif (order.status == "Prepared"):
        setattr(order, "status", "Delivered")
        filterStatus = "Prepared"
    elif (order.status == "Delivered"):
        order.delete()
        filterStatus = "Delivered"
    else:
        messages.error(request, "There was an error updating the status of this order")
    order.save()

    cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status = filterStatus)

    #sends message to customer once order is confirmed 
    customer_id = order.customerID
    messages.info(request, f"The order (#{orderID}) has been confirmed by a member of staff.")

    #message sent to the waiter notifying them of the message being delivered to the customer 
    messages.success(request, f"Message confirming this order has been sent to {customer_id}.")

    return render(request, "orders.html", {'cust_orders': cust_orders}) 

# Make http requests on page that shows menu and allows modification to the menu
def changeMenu(request):
    form_data = request.GET.copy()
    if len(form_data) > 0:
        if (MenuItem.objects.filter(name = form_data['name']).exists()):
            myItem = MenuItem.objects.get(name = form_data['name'])
            for name in form_data:
                setattr(myItem, name, form_data[name])
            myItem.save()
            messages.success(request, f'Item has successfully been updated')
        else:
            values = form_data.dict()
            values.pop('csrfmiddlewaretoken', None)
            MenuItem.objects.create(**values)
            messages.success(request, f'Item has successfully been added to the menu')

    return render(request, "changeMenu.html", {'form' : menuUpdateForm(), 'menuData': MenuItem.objects.all(),"itemToDelete" : None})

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

def viewHelpRequests(request):
    return render(request, "clientHelpRequests.html", {'help_requests' : HelpRequest.objects.all()})

def deleteOrder(request, ID):
    orders = Order.objects.all()
    order = Order.objects.get(ID=ID)
    order.delete()
    return render(request, 'orders.html', {'Orders': orders})