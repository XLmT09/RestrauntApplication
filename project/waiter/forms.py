from django import forms
from project.models import MenuItem

# This python code will be converted to an HTML form, when its rendered on the website
# by inherting from the ModelForm class.
# This form is used to update/add/delete items from the current menu
class menuUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'nameTextField','placeholder':'Enter name'}))
    price = forms.DecimalField (widget=forms.NumberInput(attrs={'placeholder':'Enter price', 'min':0,'step':0.01}))
    calories = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter calories', 'min':0}) )
    alergies = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter allergies'})) 
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'placeholder':'Enter description'}))

    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "course", "dietRequirements","alergies", "description"]
        
        
