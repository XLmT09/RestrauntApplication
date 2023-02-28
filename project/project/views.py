from django.shortcuts import render
from django.db import models
from .models import MenuItem
from .models import Order
from .models import HelpRequest
from django.contrib.auth.decorators import login_required
from . import models
from .forms import helpRequestForm
from django.contrib import messages

# The default home page for the website
def homePage(request):
    # Gets a list of all the groups a user is in
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'homePage.html', {'title': 'Home', 'user_groups' : user_groups})

def home(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'home.html')

def results(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'results.html')

@login_required
def menu(request):
    items = MenuItem.objects.all()
    # this selects the name of the web page and sends the user to that page
    return render(request, 'menu.html',{'MenuItems': items, 'helpForm': helpRequestForm()})

def ltohSort(request):
    items = MenuItem.objects.all().order_by('price')
    return render(request, 'ltohsort.html', {'MenuItems': items})


def checkout(request):
    test = request.COOKIES.get('items') 
    if len(test) == 0:
        items = MenuItem.objects.all()
    # this selects the name of the web page and sends the user to that page
        return render(request, 'menu.html',{'MenuItems': items, 'helpForm': helpRequestForm()})
        
    testArray = test.split(',')
    print(testArray)
    print("tes")
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
        i[1] =round( float(i[1]) * numberOfItems,2)
        i.append(numberOfItems)
        
    print("before")

    
    return render(request, 'checkout.html',context={'MenuItems': usedItems , 'total':price,'items':itemNumber})

def orderComplete(request):
    #Ids = request.COOKIES.get('itemIds').split(',')
    #idIntList = []
    #for id in Ids:
    #    idIntList.append(int(id))
    
    #order = models.Order(customerID=request.user,status='Placed',orderedItems=idIntList)
    #order.save()
    return render(request, 'orderComplete.html')

# add order - set status to placed




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
