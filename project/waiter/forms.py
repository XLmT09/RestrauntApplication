from django import forms


class menuUpdateForm(forms.Form):
    name = forms.CharField(label="name", max_length=20)
    price = forms.FloatField(label = "price")
    calories = forms.IntegerField(label="calories")
    cuisine = forms.CharField(label="cuisine", max_length=20)
    #ingredients
    #course
    #dietRequirements