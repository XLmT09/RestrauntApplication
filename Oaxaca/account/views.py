from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'login.html', {'title': 'Login'})

def signup(request):
    # Get data which user entered into form, when they click submit
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Store values in the field directly to the database
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
        # If the user clicks submit but data wasnt valid
        else:
            messages.error(request, f'Account failed to be created!')
    # Load a form for the user
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form, 'title':'Sign Up'})

#user must be logged in to use this page
@login_required
def profile(request):
    return render(request, 'profile.html', {'title': 'Profile'})