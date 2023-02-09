from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.db import models
from .models import MenuItem, Order

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

def ltohSort(request):
    items = MenuItem.objects.all().order_by('price')
    return render(request, 'ltohsort.html', {'MenuItems': items})

def htolSort(request):
    items = MenuItem.objects.all().order_by('-price')
    return render(request, 'htolsort.html', {'MenuItems': items})

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'Orders': orders})

def deleteOrder(request, ID):
    order = Order.objects.get(ID=ID)
    order.delete()
    return HttpResponseRedirect(reverse('orders'))