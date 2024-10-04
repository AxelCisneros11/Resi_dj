from django.shortcuts import render, redirect
from .models import Campaña
from .forms import  campañaForm
from django.contrib.auth.decorators import login_required

def index(request):
    msj = Campaña.objects.all()
    context = {'msj': msj}
    return render(request, 'campaña/index.html', context)


def agregar(request):
    if request.method == 'POST':
        form = campañaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = campañaForm()  # Esto asegura que si es GET, se muestre el formulario vacío
    
    context = {'form': form}
    return render(request, 'campaña/agregar.html', context)  # Siempre retorna una respuesta
@login_required
def eliminar(request,  campaña_id):
    campaña = Campaña.objects.get(id=campaña_id)
    campaña.delete()
    return redirect('index')

def editar(request, campaña_id):
    campaña = Campaña.objects.get(id=campaña_id)
    if request.method == "POST":
        form = campañaForm(request.POST, instance=campaña)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
            form = campañaForm(instance=campaña)
            
    context = {"form" : form }
    return render(request,  "campaña/editar.html", context)
