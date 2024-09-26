from django import forms
from .models import Campaña

class campañaForm(forms.ModelForm):
    class Meta:
        model = Campaña
        fields = ['campaña','mensaje']   