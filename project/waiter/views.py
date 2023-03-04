from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem, Order, HelpRequest
from .models import Payment, TableServer
from decerators import group_required

# Make http requests to the waiter page
@group_required("Waiters")
def staff(request):
    return render(request, "waiterHome.html", {'title' : 'staff'})

# Make http requests on page that gives list of customer orders
@group_required("Waiters")
def viewOrders(request, orderStatus):
    cust_orders = None
    # If waiter wants to see NON PLACED orders, then only get orders the waiter is assigned to
    # However if order is placed then, just show all the customer orders
    if orderStatus != "Placed":
        # Get all tables which the waiter is serving
        table_orders = TableServer.objects.filter(waiterID=request.user)   
        # Get the order ids of the tables the waiter is serving
        order_ids = table_orders.values_list('orderID', flat=True)
        # Use the order ids to retrive only order info which waiter servers
        cust_orders = Order.objects.filter(ID__in=order_ids, status=orderStatus).order_by('timeOfOrder')
    else:
        # retrive all customer orders from oldest to newest
        cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status = orderStatus)

    return render(request, "orders.html", {'cust_orders': cust_orders})

# Update the order status of an customer order
@group_required("Waiters")
def updateOrderStatus(request, orderID):
    # Grab the order the user wants to chnage
    order = Order.objects.get(ID = orderID)
    # Order status will change state in this function so record inital state for that
    orderStatusBefore = order.status

    if order.status == "Placed":
        # Change order status from placed to confirmed
        setattr(order, "status", "Confirmed")
        # Assign waiter to this order using TableServer table
        # The decerator above guarntees the user will be a waiter, so simply call request.user
        table = TableServer.objects.create(orderID = order, waiterID = request.user)
        table.save()
        messages.info(request, f"Order #{orderID} has been Confirmed.")
    elif order.status == "Prepared": 
        # Change order status from perepared to delivered
        setattr(order, "status", "Delivered")
        messages.info(request, f"Order #{orderID} has been Delivered.")
    elif order.status == "Delivered": 
        order.delete()
        messages.info(request, f"Order #{orderID} has been Deleted.")
    else: 
        messages.error(request, "There was an error updating the status of this order.")

    order.save()

    # Refresh the page so waiter cant see order ehich chnaged status
    # Use the recorded status to stay on the same page
    return redirect(reverse('viewOrders', kwargs={'orderStatus': orderStatusBefore}))

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
    order = Order.objects.get(ID=ID)
    order.delete()
    placed_orders = Order.objects.all().order_by('timeOfOrder').filter(status = "Placed")
    return render(request, 'orders.html', {'cust_orders': placed_orders})

def customer_payments(request):
    all_payments = Payment.objects.all()
    totalIncome = 0
    for payment in all_payments:
        totalIncome += payment.paymentAmount
    return render(request, "paymentInfo.html", {'cust_payments':all_payments,'income':totalIncome})