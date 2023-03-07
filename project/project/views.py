from django.shortcuts import redirect, render
from django.db import models
from .models import MenuItem
from .models import Order
from .models import HelpRequest
from waiter.models import Payment
from django.contrib.auth.decorators import login_required
from . import models
from .forms import helpRequestForm
from django.http import HttpResponse
from django.contrib import messages

def notificationOrders(request):
    try:
        Orders = Order.objects.filter(customerID_id=request.user,notificationSent=False)
        statusList =[]
        for i in Orders:
            statusList.append(i.status)

            print(i.status)
        
        return statusList
        
    except:
        Orders = ''
        return Orders





# The default home page for the website
def homePage(request):
    Orders =  notificationOrders(request)
    
        #obj.some_field = some_var
        #obj.save()
    # Gets a list of all the groups a user is in
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'homePage.html', {'title': 'Home', 'user_groups' : user_groups,'orders':Orders})

def home(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'home.html')

def results(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'results.html')

@login_required
def menu(request):
    items = MenuItem.objects.all()
    cookieData = request.COOKIES.get('items')
    print("Data=",cookieData)
    print(request.COOKIES.get('itemIds'))
    print(request.COOKIES.get('itemWithIds'))
    basketPrice = 0
    itemDict = dict()
    if cookieData != None:
        cookieData = cookieData.split(",")
        for i in range(len(cookieData)):
            if i % 2 == 0:
                itemName = cookieData[i]
                if itemName in itemDict:
                    itemDict[itemName] += 1
                else:
                    itemDict[itemName] = 1
            else:
                basketPrice += float(cookieData[i])
    print("DICT=",itemDict)
    basketPriceStr = "{:.2f}".format(basketPrice)
    # this selects the name of the web page and sends the user to that page
    return render(request, 'menu.html',{'MenuItems': items, 'helpForm': helpRequestForm(),"basketTotal":basketPriceStr, "itemDict": itemDict})

def ltohSort(request):
    items = MenuItem.objects.all().order_by('price')
    return render(request, 'ltohsort.html', {'MenuItems': items})


def checkout(request):
    test = request.COOKIES.get('items') 
    print("test=",test)
    if len(test) == 0:
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

        price = "{:.2f}".format(price)

        return render(request, 'checkout.html',context={'MenuItems': usedItems , 'total':price,'items':itemNumber})


def orderComplete(request):
    return render(request, 'orderComplete.html')


def htolSort(request):
    items = MenuItem.objects.all().order_by('-price')
    return render(request, 'htolsort.html', {'MenuItems': items})

def customerOrder(request):
    Orders = Order.objects.filter(customerID_id=request.user)

    return render(request, 'customerOrders.html',{'Orders':Orders})
    



def sendHelpRequest(request):
    form_data = request.GET.copy()
    form_message = form_data['message']

    if (form_message == ""):
        form_message = None

    current_user = request.user
    HelpRequest.objects.create(customerID = current_user, message = form_message)

    messages.success(request, f'Your request has been sent successfully')

    return render(request, 'menu.html',{'MenuItems': MenuItem.objects.all(), 'helpForm': helpRequestForm()})

def clientHelpRequests(request):
    help_requests = HelpRequest.objects.all()
    return render(request, 'clientHelpRequests.html', {'help_requests': help_requests})





def completePayment(request):
    orderedItems = request.COOKIES.get('items').split(",")
    itemDict = dict()
    orderCost = 0
    for i in range(len(orderedItems)):
        if i % 2 == 0:
            itemName = orderedItems[i]
            if itemName in itemDict:
                itemDict[itemName] += 1
            else:
                itemDict[itemName] = 1
        else:
            orderCost += float(orderedItems[i])

    order = models.Order(customerID=request.user,status='Placed',orderedItems=itemDict)
    order.save()

    newPayment = Payment.objects.create(customerID = request.user, orderID = order, paymentAmount = orderCost)
    newPayment.save()

    return render(request,'completePayment.html')


def testNotification(request):
    return render(request,'testNotification.html')



