from django.forms import ModelForm
from .models import Produit
from .models import Fournisseur
from django import forms
class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" #pour tous les champs de la table
        #fields=['libelle','description'] #pour qulques champs


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }
