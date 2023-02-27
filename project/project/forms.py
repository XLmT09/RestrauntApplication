from django import forms
from django.db import models
from project.models import MenuItem
from project.models import HelpRequest
from django.contrib.postgres.fields import ArrayField
from project.models import Order
from django.contrib.auth.models import User

class menuUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'nameTextField'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "course", "dietRequirements","alergies", "description"]


class helpRequestForm(forms.ModelForm):
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows' : 3, 'placeholder' : 'Enter message (optional)'}))
    class Meta:
        model = HelpRequest
        fields = ["message"]
        

        
        


