from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('<h1>Login</h1>')

def signup(request):
    return HttpResponse('<h1>Create Account</h1>')