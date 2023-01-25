from django.shortcuts import render
from django.http import JsonResponse
from. import nutritionPopUp

foodList = [nutritionPopUp.item("food","55"),nutritionPopUp.item("food3","65"),nutritionPopUp.item("food2",75),
            nutritionPopUp.item("food","55"),nutritionPopUp.item("food3","65"),nutritionPopUp.item("food2",75),
            nutritionPopUp.item("food","55"),nutritionPopUp.item("food3","65"),nutritionPopUp.item("food2",75),
            nutritionPopUp.item("food","55"),nutritionPopUp.item("food3","65"),nutritionPopUp.item("food2",75),
            nutritionPopUp.item("food","55"),nutritionPopUp.item("food3","65"),nutritionPopUp.item("food2",75)]
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


