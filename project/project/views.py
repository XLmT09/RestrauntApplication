from django.shortcuts import render
from django.http import JsonResponse
from. import nutritionPopUp
x=nutritionPopUp.item("Test","55,","testing","78","none","Starter")
y=nutritionPopUp.item("Test","55,","testing","78","none","Main")
i=nutritionPopUp.item("Test","55,","testing","78","none","Main")
p=nutritionPopUp.item("Test","55,","testing","78","none","Main")
s=nutritionPopUp.item("Test","55,","testing","78","none","Main")
z=nutritionPopUp.item("Test","55,","testing","78","none","Dessert")
m=nutritionPopUp.item("Test","55,","testing","78","none","Side")
o=nutritionPopUp.item("Test","55,","testing","78","none","Drink")
foodList = [x,y,z,m,o,i,p,s]
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
    # this selects the name of the web page and sends the user to that page
    return render(request, 'menu.html',context={'data': foodList})


