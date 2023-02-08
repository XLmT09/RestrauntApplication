from django import forms
from django.db import models
from project.models import MenuItem

class menuUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "cuisine", "ingredients", "course", "dietRequirements","alergies", "description"]