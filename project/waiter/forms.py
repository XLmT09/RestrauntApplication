from django import forms

class menuUpdateForm(forms.Form):
    name = forms.CharField(label="name", max_length=20)