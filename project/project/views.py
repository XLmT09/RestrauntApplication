from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from .models import MenuItem

def homePage(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'homePage.html', {'title': 'Home'})

def home(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'home.html')

def results(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'results.html')

def menu(request):
    items = MenuItem.objects.all()
    # this selects the name of the web page and sends the user to that page
    return render(request, 'menu.html',{'MenuItems': items})


def checkout(request):
    test = request.COOKIES.get('test') 
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


# add order - set status to placed



