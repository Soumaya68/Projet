from django import forms
from .models import Vehicule

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['marque', 'date_achat', 'nb_places', 'description', 'longueur', 'climatisation']
