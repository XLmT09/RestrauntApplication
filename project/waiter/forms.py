from django import forms
from django.db import models
from project.models import MenuItem

class menuUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'nameTextField'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "ingredients", "course", "dietRequirements","alergies", "description"]