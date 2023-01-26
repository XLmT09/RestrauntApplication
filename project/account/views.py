from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'account/login.html', {'title': 'Login'})

def signup(request):
    # Get data which user entered into form, when they click submit
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Store values in the field directly to the database
            print(form.cleaned_data["role"])
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
        # If the user clicks submit but data wasnt valid
        else:
            messages.error(request, f'Account failed to be created!')
    # Load a form for the user
    else:
        form = UserRegisterForm()
    return render(request, 'account/signup.html', {'form': form, 'title':'Sign Up'})

#user must be logged in to use this page
@login_required
def profile(request):
    if (User.role == "Customer"):
        return render(request, "account/customerPage.html", {'title' : 'profile'})
    else:
        return render(request, "account/staffPage.html", {'title' : 'profile'})
    #return render(request, 'account/profile.html', {'title': 'Profile'})

def staff(request):
    return render(request, "staffPage.html", {'title' : 'staff'})