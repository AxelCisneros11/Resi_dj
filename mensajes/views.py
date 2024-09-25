from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import  mensajeForm

def home(request):
    msj = Mensaje.objects.all()
    context = {'msj': msj}
    return render(request, 'mensajes/home.html', context)

def msjAgregar(request):
    if request.method == 'POST':
        form = mensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = mensajeForm()  # Esto asegura que si es GET, se muestre el formulario vacío
    
    context = {'form': form}
    return render(request, 'mensajes/msjAgregar.html', context)  # Siempre retorna una respuesta

def msjEliminar(request,  mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id)
    mensaje.delete()
    return redirect('home')

def msjEditar(request, mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id)
    if request.method == "POST":
        form = mensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
            form = mensajeForm(instance=mensaje)
            
    context = {"form" : form }
    return render(request,  "mensajes/msjEditar.html", context)

