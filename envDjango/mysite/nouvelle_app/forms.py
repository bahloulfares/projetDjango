from django import forms
from .models import Tache

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'termine']
        widgets = {
            'termine': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }
