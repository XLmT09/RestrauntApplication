from django import forms
from django.db import models
from project.models import MenuItem

COURSES = [
    ('Starter','Starter'),
    ('Main','Main'),
    ('Dessert','Dessert'),
    ('Side','Side'),
    ('Drink','Drink')
]

DIETREQUIREMENTS = [
    ('None', 'None'),
    ('Vegan', 'Vegan'),
    ("Vegetarian", "Vegetarian")
]


class menuUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "cuisine", "ingredients", "course", "dietRequirements"]
        
        def delete(self, comit=True):
            self.instance.delete()
            if comit:
                self.instance.save()