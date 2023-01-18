from django.shortcuts import render

def homePage(request):
    # this selects the name of the web page and sends the user to that page
    return render(request, 'homePage.html')