from django.shortcuts import render

def display_results(request):
    return render(request, 'results.html');