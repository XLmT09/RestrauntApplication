from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''
This class creates a UserRegistration from which inherits from the
UserCreationForm, by default the UserCreationForm has a username,
password and confirm password field.
This class will inherit this form but also add extra fields.
'''
class UserRegisterForm(UserCreationForm):
    # This class states which model should be used to create this form
    class Meta:
        model = User
        # The fields that will be shown on the webpage
        # This also represents the ORDER the fields will be shown on the webpage
        fields = ['username', 'email', 'password1', 'password2']