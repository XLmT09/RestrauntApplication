from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from decerators import login_required
from project.models import Order, MenuItem
from project.views import checkout

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

#user must be logged in to use the below pages
@login_required
def profile(request):
    # Render the webpage for displaying profile information
    return render(request, 'account/profile.html', {'title': 'Profile'})

@login_required
def userInformation(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    return render(request, 'account/information.html', {'title':'Information', 'user_groups' : user_groups})

@login_required
def userOrders(request):
    Orders = Order.objects.filter(customerID_id=request.user)

    return render(request, 'account/userOrders.html', {'title':'Old Orders', 'Orders':Orders})

def redoOrder(request):
    test = request.COOKIES.get('items')
    print(test)

    return redirect(checkout)