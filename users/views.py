from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': CustomUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio o donde desees
            else:
                return render(request, 'signup.html', {'form': form, 'error': 'Formulario no válido'})
        return render(request, 'signup.html', {'form': CustomUserCreationForm(), 'error': 'Las contraseñas no coinciden'})
   

def  signout(request):
    logout(request)
    return redirect('home')

#metodo para retornar el LOGIN 
def signin(request):
    if request.method == 'GET' :
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')