from django.shortcuts import redirect, render
from django.db import models
from .models import MenuItem
from .models import Order
from .models import HelpRequest
from waiter.models import Payment
from decerators import login_required
from . import models
from .forms import helpRequestForm
from django.contrib import messages
from django.utils.timezone import localdate

def notificationOrders(request):
    # If user is not logged in then empty string is returned
    try:
        Orders = Order.objects.filter(customerID_id=request.user,notificationSent=False)
        statusList =[]
        for i in Orders:
            statusList.append(str(i.status))
            print(i.status)
        
        Order.objects.filter(customerID_id=request.user,notificationSent=False).update(notificationSent=True)
        
        return statusList
        
    except:
        Orders = ''
        return Orders
    
# The default home page for the website
def homePage(request):
    Statuses =  notificationOrders(request)
    
        #obj.some_field = some_var
        #obj.save()
    # Gets a list of all the groups a user is in
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'homePage.html', {'title': 'Home', 'user_groups' : user_groups,'statuses':Statuses})

@login_required
def menu(request):
    Statuses =  notificationOrders(request)
    # Retrieve all MenuItems from the database
    items = MenuItem.objects.all()
    basketPriceStr,itemDict = getPriceOfBasket(request)
    # this selects the name of the web page and sends the user to that page
    return render(request, 'menu.html',{'MenuItems': items, 'helpForm': helpRequestForm(),"basketTotal":basketPriceStr, "itemDict": itemDict,'statuses':Statuses,'sortValue':'dlt'})

def getPriceOfBasket(request):
    # Retrieve data from 'items' cookie
    cookieData = request.COOKIES.get('items')
    basketPrice = 0
    itemDict = dict()
    if cookieData != None:
        cookieData = cookieData.split(",")
        for i in range(len(cookieData)):
            if i % 2 == 0:
                # Get name of next item in cookie data
                itemName = cookieData[i]
                # Check if the item is already in the dictionary
                if itemName in itemDict:
                    # Increment the counter for the given item by 1
                    itemDict[itemName] += 1
                else:
                    # Create a new dictionary entry with initial value 1
                    itemDict[itemName] = 1
            else:
                # Increment the total basket price by the price of the next item
                basketPrice += float(cookieData[i])
    #Format the basket price so that it displays to 2dp
    basketPriceStr = "{:.2f}".format(basketPrice)
    return basketPriceStr,itemDict

@login_required
def ltohSort(request):
    Statuses =  notificationOrders(request)
    items = MenuItem.objects.all().order_by('price')
    basketPriceStr,itemDict = getPriceOfBasket(request)
    return render(request, 'menu.html',{'MenuItems': items, 'helpForm': helpRequestForm(),"basketTotal":basketPriceStr, "itemDict": itemDict,'statuses':Statuses,'sortValue':'ltoh'})

def checkout(request):
    Statuses =  notificationOrders(request)
    test = request.COOKIES.get('items') 
    if len(test) == 0:
        # Redirect the user to the menu page if the basket is empty
        return redirect(menu)
    else:
        testArray = test.split(',')
        itemArray=[]
        usedItems = []
        price = 0
        itemNumber = 0
        for i in range(0, len(testArray)):
            if(i%2 ==0):
                tempArray = []
                tempArray.append(testArray[i])
                tempArray.append(testArray[i+1])
                price = price + float(testArray[i+1])
                itemArray.append(tempArray)
                
        for i in itemArray:
            if not (i in usedItems):
                usedItems.append(i)
        for i in usedItems:
            numberOfItems = itemArray.count(i)
            itemNumber = itemNumber + numberOfItems
            i[1] = "{:.2f}".format(float(i[1]) * numberOfItems)
            i.append(numberOfItems)

        # Format the price so that it is displayed to 2dp
        price = "{:.2f}".format(price)
        # Render the webpage for displaying the checkout
        return render(request, 'checkout.html',context={'MenuItems': usedItems , 'total':price,'items':itemNumber,'statuses':Statuses})


def orderComplete(request):
    Statuses =  notificationOrders(request)
    return render(request,'orderComplete.html',context={'statuses':Statuses})

@login_required
def htolSort(request):
    Statuses =  notificationOrders(request)
    items = MenuItem.objects.all().order_by('-price')
    basketPriceStr,itemDict = getPriceOfBasket(request)
    return render(request, 'menu.html',{'MenuItems': items, 'helpForm': helpRequestForm(),"basketTotal":basketPriceStr, "itemDict": itemDict,'statuses':Statuses,'sortValue':'htol'})


def customerOrder(request):
    Statuses =  notificationOrders(request)
    Orders = Order.objects.filter(customerID_id=request.user)

    return render(request, 'customerOrders.html',{'Orders':Orders,'statuses':Statuses})
    


# This method creates a new HelpRequest object in the database
def sendHelpRequest(request):
    # Retrieve the entered data fromn the help request form
    form_data = request.GET.copy()
    # Retrive the entered message from the form data
    form_message = form_data['message']
    # Check if the user has entered a message in the form
    if (form_message == ""):
        form_message = None
    # Retrieve the ID of the currently signed in user
    current_user = request.user
    # Create a new HelpRequest object with the given message for the given user
    HelpRequest.objects.create(customerID = current_user, message = form_message)
    # Display a message stating that the help request was successfully sent
    messages.success(request, f'Your request has been sent successfully')
    # Render the menu web page and close the popup containing the help request form
    #return render(request, 'menu.html',{'MenuItems': MenuItem.objects.all(), 'helpForm': helpRequestForm()})
    return redirect(menu)

def clientHelpRequests(request):
    # Render the webpage for displaying all customer help requests to the waiter
    return render(request, 'clientHelpRequests.html', {'help_requests': HelpRequest.objects.all()})

def completePayment(request):
    # Retrieve all the ordered items from cookie data
    orderedItems = request.COOKIES.get('items').split(",")
    itemDict = dict()
    orderCost = 0
    for i in range(len(orderedItems)):
        if i % 2 == 0:
            # Get name of next item in cookie data
            itemName = orderedItems[i]
            # Check if the item is already in the dictionary
            if itemName in itemDict:
                # Increment the counter for the given item by 1
                itemDict[itemName] += 1
            else:
                # Create a new dictionary entry with initial value 1
                itemDict[itemName] = 1
        else:
            # Increment the total order cost by the price of the next item
            orderCost += float(orderedItems[i])
    # Create a new Order object with the items which have been ordered
    order = models.Order(customerID=request.user,status='Placed',orderedItems=itemDict)
    # Save the new Order object to the database
    order.save()
    # Create a new Payment object which includes the total price of the order
    newPayment = Payment.objects.create(customerID = request.user, orderID = order, paymentAmount = orderCost)
    # Save the new payment object to the database
    newPayment.save()
    # Render the webpage stating that the order has successfully been placed
    messages.success(request, f"Thank you for your Order, we will notify you as your order is processed")
    return redirect(homePage)


def testNotification(request):
    return render(request,'testNotification.html')


def cleanupDatabase():
    # Retrieve the current system date
    currentDate = localdate()
    # Retrieve all orders from the database
    all_orders = Order.objects.all()
    for order in all_orders:
        # Check to see if the date of the order matches the current date of the system
        if order.dateOfOrder != currentDate:
            # Delete the payment linked to the given order from the database
            payment = Payment.objects.get(orderID = order.ID)
            payment.delete()
            # Delete the order from the database
            order.delete()
    
def deleteExcessDeliveries():
    # deletes the earliest delivered orders so that only (at most) 20 orders exist on the system
    # fetches how many "excess" delivered orders there are - "excess" means if there is a delivered order count above 20
    delivered_orders = Order.objects.all().filter(status = "Delivered")
    excess_orders_num = delivered_orders.count() - 20
        
    if (excess_orders_num > 0):
        excess_orders = delivered_orders[:excess_orders_num]
        excess_orders.delete()