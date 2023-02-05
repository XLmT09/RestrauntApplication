from django import forms
from django.db import models
from project.models import MenuItem

class menuUpdateForm(forms.ModelForm):

    dropDown = forms.ModelMultipleChoiceField(queryset=MenuItem.objects.all())

    class Meta:
        model = MenuItem
        fields = ["name", "price", "calories", "cuisine", "ingredients", "course", "dietRequirements"]

    class Meta:
        model = MenuItem
        def delete(self, comit=True):
            self.instance.delete()
            if comit:
                self.instance.save()