from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''
When creating drop down list option for the form class, it must be a
list of tuples. First param is the key and the the second param 
is the text that will be shown on the webpage.
'''
ROLES = [
        ('customer', 'Customer'),
        ('kitchenStaff', 'Kitchen Staff'),
        ('waiter', 'Waiter')
        ]

'''
This class creates a UserRegistration from which inherits from the
UserCreationForm, by default the UserCreationForm has a username,
password and confirm password field.
This class will inherit this form but also add extra fields.
'''
class UserRegisterForm(UserCreationForm):
    # Email field
    email = forms.EmailField()
    #Drop down list field
    role = forms.CharField(label = 'Select your role:', widget = forms.Select(choices = ROLES))

    # This class states which model should be used to create this form
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']