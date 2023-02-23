from django import forms
from django.db import models
from project.models import MenuItem
from project.models import Order

class menuUpdateForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'id':'nameTextField','placeholder':'Enter name'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter price'}))
    calories = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter calories'}))
    alergies = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter allergies'})) 
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'placeholder':'Enter description'}))

    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "course", "dietRequirements","alergies", "description"]
        
        
