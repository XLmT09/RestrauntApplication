from django.shortcuts import render

def homePage(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'homePage.html', {'title': 'Home'})

def home(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'home.html')

def results(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'results.html')