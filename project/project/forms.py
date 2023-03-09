from django import forms
from django.db import models
from project.models import MenuItem
from project.models import HelpRequest
from django.contrib.postgres.fields import ArrayField
from project.models import Order
from django.contrib.auth.models import User

# A django form for updating and altering items on the menu
class menuUpdateForm(forms.ModelForm):
    #Define the widgets that will be displayed on the form
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'nameTextField'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        # Define the associated django model
        model = MenuItem
        # Define the attributes/fields of the associated model
        fields = ["name", "price", "calories", "course", "dietRequirements","alergies", "description"]


class helpRequestForm(forms.ModelForm):
    #Define the widgets that will be displayed on the form
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows' : 3, 'placeholder' : 'Enter message (optional)'}))
    class Meta:
        # Define the associated django model
        model = HelpRequest
        # Define the attributes/fields of the associated model
        fields = ["message"]
        

        
        


