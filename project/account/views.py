from django.shortcuts import render, redirect
from .forms import UserRegisterForm
# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def signup(request):
    # Get data which user entered into form, when they click submit
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Store values in the field directly to the database
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('account-login')
    # Load a form for the user
    else:
        form = UserRegisterForm()
    return render(request, 'account/signup.html', {'form': form})