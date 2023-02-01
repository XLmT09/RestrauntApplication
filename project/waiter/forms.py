from django import forms

INGREDIENTS = [
    ("Meat", "Meat"),
    ("Cheese", "Cheese"),
    ("Vegetables", "Vegetables")
]

COURSE = [
    ("Starter", "Starter")
    ("Main", "Main"),
    ("Dessert", "Dessert")
]

DIET = [
    ("None", "None"),
    ("Vegeterian","Vegeterian"),
    ("Pesciterian","Pesciterian")
]

class menuUpdateForm(forms.Form):
    name = forms.CharField(label="name", max_length=20)
    price = forms.FloatField(label = "price")
    calories = forms.IntegerField(label="calories")
    cuisine = forms.CharField(label="cuisine", max_length=20)
    ingredients = forms.CharField(label = 'Select ingredients', widget = forms.Select(choices = INGREDIENTS))
    course = forms.CharField(label = 'Select course', widget = forms.Select(choices = COURSE))
    dietRequirements = forms.CharField(label = 'Select dietary requirements', widget = forms.Select(choices = DIET))