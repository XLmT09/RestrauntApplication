from django.shortcuts import render

def order(request):
    return render(request, 'order.html', {'title': 'Kitchen Staff Orders'})