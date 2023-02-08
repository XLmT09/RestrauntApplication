from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem
from django.core import serializers
import json

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

    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all()})

def deleteItem(request):
    if request.method == 'POST':
        form = menuUpdateForm(request.POST)
        if 'Delete Item' in request.POST:
            menu_item = MenuItem.objects.filter(name=form.data['name']   )
        if menu_item.exists():
            menu_item.delete()
            return redirect('changeMenu.html')
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all()})

def refreshMenu(request, item):
    if item == None:
        form = menuUpdateForm()
    else:
        form = menuUpdateForm(instance=MenuItem.objects.get(name=item))
    return render(request, "changeMenu.html", {'form' : form, 'menuData': MenuItem.objects.all()})



# need to:
# pull changes to DB table
# add/update form fields accordingly
# make sure form can still be submitted without error
