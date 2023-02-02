from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import menuUpdateForm
from project.models import MenuItem

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



