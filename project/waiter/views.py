from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem
from django.core import serializers
import json
from django.urls import resolve

# Create your views here.

def staff(request):
    return render(request, "staffPage.html", {'title' : 'staff'})

def viewOrders(request):
    return render(request, "viewOrders.html")

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
    print("deleting", itemToDelete)
    if itemToDelete == None:
        messages.error(request, f'No item selected to delete')
    else:
        MenuItem.objects.filter(name=itemToDelete).delete()
        messages.success(request, f'Item has successfully been deleted')
    form = menuUpdateForm()
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all(), "itemToDelete" : None})

def refreshMenu(request, item):
    if item == None:
        form = menuUpdateForm()
    else:
        form = menuUpdateForm(instance=MenuItem.objects.get(name=item))
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all(), 'itemToDelete': item})



# need to:
# pull changes to DB table
# add/update form fields accordingly
# make sure form can still be submitted without error
