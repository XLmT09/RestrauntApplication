from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# This view handles all HTTP requests and responses for the sign up page
def signup(request):
    # Get data which user entered into form, when they click submit
    if request.method == 'POST':
        # Extract the data as a dictionary which the user put in the form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Store values in the field directly to the database
            form.save()
            # extract the username from the form to dispaly a message to the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
        else:
            # If the user clicks submit but data wasnt valid
            messages.error(request, f'Account failed to be created!')
    else:
        # Load a form for the user
        form = UserRegisterForm()
    return render(request, 'account/signup.html', {'form': form, 'title':'Sign Up'})

#user must be logged in to use this page
@login_required
def profile(request):
    return render(request, 'account/profile.html', {'title': 'Profile'})