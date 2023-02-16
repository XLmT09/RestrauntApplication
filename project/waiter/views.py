from django.shortcuts import render
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem
from project.models import Order
from django.shortcuts import redirect

# Make http requests to the waiter page
def staff(request):
    return render(request, "staffPage.html", {'title' : 'staff'})

# Make http requests on page that gives list of customer orders
def viewOrders(request, orderStatus):
    # retrive all customer orders from oldest to newest
    cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status = orderStatus)

    return render(request, "orders.html", {'cust_orders': cust_orders})



def updateOrderStatus(request):
    orderID = request.COOKIES.get('chosenOrderID')
    order = Order.objects.get(ID = orderID)

    if (order.status == "Placed"):
        setattr(order, "status", "Confirmed")
        filterStatus = "Placed"
    order.save()

    cust_orders = Order.objects.all().order_by('timeOfOrder').filter(status = filterStatus)

    #sends message to customer once order is confirmed 
    customer_id = order.customerID
    messages.info(request, f'The order (#{orderID}) has been confirmed by a member of staff.')

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
