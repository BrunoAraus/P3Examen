from django.shortcuts import render, redirect
from core.forms import PlatoForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html',{'form':form})




def home(request):
    contexto = {'plato': Plato.objects.all()}
    return render(request, 'core/index.html',contexto)

def Gestionar(request):
    contexto = {'plato': Plato.objects.all()}
    return render(request, 'core/Gestionar.html',contexto)

def usuario(request):
    return render(request, 'core/usuario.html')

def historial(request):
    return render(request, 'core/historial.html')

def pedido(request):
    return render(request, 'core/pedido.html')


def CrearPlato(request):
    contexto = {'form': PlatoForm()}
    if request.method == "POST":
        Plato = PlatoForm(request.POST)
        if Plato.is_valid:
            Plato.save()
            contexto["mensaje"] = "Plato agregado!."
    return render(request, 'core/CrearPlato.html', contexto)

def modificarPlato(request, id):
    plato = Plato.objects.get(nombre=id)
    contexto = {'form': PlatoForm(instance=plato)}
    if request.method == "POST":
        plato = PlatoForm(request.POST, instance=plato)
        if plato.is_valid:
            plato.save()
            contexto["mensaje"] = "plato modificado!."
            contexto['form'] = plato
    return render(request, 'core/modificarPlato.html', contexto)

def eliminarPlato(request, id):
    plato = Plato.objects.get(nombre=id)
    plato.delete()
    return redirect(to="Gestionar")


def producto(request, id):
    plato = Plato.objects.get(nombre=id)
    contexto = {'plato': plato}
    return render(request, 'core/producto.html', contexto)