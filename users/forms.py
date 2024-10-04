# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    numerodetelefono = forms.NumberInput()
    division = forms.TextInput()
    zona = forms.TextInput()
    agencia = forms.TextInput()

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'numerodetelefono', 'division', 'zona', 'agencia', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.numerodetelefono = self.cleaned_data['numerodetelefono']
        user.division = self.cleaned_data['division']
        user.zona = self.cleaned_data['zona']
        user.agencia = self.cleaned_data['agencia']
        if commit:
            user.save()
        return user
