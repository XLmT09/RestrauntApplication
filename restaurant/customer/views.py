from django.shortcuts import render

def display_home(request):
    return render(request, 'home.html');