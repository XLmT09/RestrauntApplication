from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from .models import MenuItem
from django.contrib.auth.decorators import login_required
import time
from . import Database

def homePage(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'homePage.html', {'title': 'Home'})

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
    return render(request, 'menu.html',{'MenuItems': items})


def checkout(request):
    test = request.COOKIES.get('items') 
    if len(test) == 0:
        items = MenuItem.objects.all()
    # this selects the name of the web page and sends the user to that page
        return render(request, 'menu.html',{'MenuItems': items})
        
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
    return render(request, 'checkout.html',context={'MenuItems': usedItems , 'total':price,'items':itemNumber})

def orderComplete(request):
    itemIds = request.COOKIES.get('itemIds') 
    userId = request.COOKIES.get('userId') 
    print(type(itemIds))
    print(type(userId))
    idList = itemIds.split(',')
    idIntList=[]
    for i in idList:
        idIntList.append(int(i))
        
    database = Database.Database()
    maxId = database.executeQueryGet(database.connect(),'SELECT MAX("ID") FROM "Order";',True)
    database.executeQueryGet(database.connect(),'INSERT INTO "Order" ("ID", "customerID_id","status","timeOfOrder","orderedItems")VALUES (3,4,"Placed","21:11:17","4,4");',False)
    

    newTime = time.localtime()
    current_time = time.strftime("%H:%M:%S", newTime)
    new_entry = models.Order(ID= (maxId +1) , customerID=int(userId),status="Placed",timeOfOrder=current_time,orderedItems=idIntList)
    new_entry.save()


    

    return render(request, 'orderComplete.html')

# add order - set status to placed



