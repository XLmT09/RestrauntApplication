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
    dropDown = forms.ModelMultipleChoiceField(queryset=MenuItem.objects.all())

    name = forms.CharField(widget=forms.TextInput(attrs={'id':'nameField'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'id':'priceField'}))
    calories = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'caloriesField'}))
    cuisine = forms.CharField(widget=forms.TextInput(attrs={'id':'cuisineField'}))
    ingredients = forms.CharField(widget=forms.TextInput(attrs={'id':'ingredientsField'}))
    course = forms.CharField(widget=forms.Select(choices=COURSES,attrs={'id':'courseField'}))
    dietRequirements = forms.CharField(widget=forms.Select(choices=DIETREQUIREMENTS,attrs={'id':'dietRequirementsField'}))

    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "cuisine", "ingredients", "course", "dietRequirements"]