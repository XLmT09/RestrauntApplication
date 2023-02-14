from django.shortcuts import render

def order(request):
    return render(request, 'kitchen/order.html', {'title': 'Kitchen Staff Order'})