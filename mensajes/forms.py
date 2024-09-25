from django import forms
from .models import Mensaje

class mensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['mensaje']   