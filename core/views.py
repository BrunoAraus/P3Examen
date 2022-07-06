from django.shortcuts import render, redirect
from core.forms import ProductoForm, SuscripcionForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponse


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
    contexto = {'producto': Producto.objects.all()}
    return render(request, 'core/index.html',contexto)

def Gestionar(request):
    contexto = {'producto': Producto.objects.all()}
    return render(request, 'core/Gestionar.html',contexto)

def usuario(request):
    return render(request, 'core/usuario.html')

def historial(request):
    return render(request, 'core/historial.html')

def pedido(request):
    return render(request, 'core/pedido.html')


def CrearProducto(request):
    contexto = {'form': ProductoForm()}
    if request.method == "POST":
        Producto = ProductoForm(request.POST)
        if Producto.is_valid:
            Producto.save()
            contexto["mensaje"] = "Producto agregado!."
    return render(request, 'core/CrearProducto.html', contexto)

def modificarProducto(request, id):
    producto = Producto.objects.get(nombre=id)
    contexto = {'form': ProductoForm(instance=producto)}
    if request.method == "POST":
        producto = ProductoForm(request.POST, instance=producto)
        if producto.is_valid:
            producto.save()
            contexto["mensaje"] = "producto modificado!."
            contexto['form'] = producto
    return render(request, 'core/modificarProducto.html', contexto) 

def eliminarProducto(request, id):
    producto = Producto.objects.get(nombre=id)
    producto.delete()
    return redirect(to="Gestionar")


def producto(request, id):
    producto = Producto.objects.get(nombre=id)
    contexto = {'producto': producto}
    return render(request, 'core/producto.html', contexto)

def descontar(request, id):
    producto = Producto.objects.get(nombre=id)
    producto.stock = producto.stock - 1
    producto.save()
    return redirect(to="home")

def descuento(request,id):
    producto = Producto.objects.get(nombre=id)
    producto.precio_final = producto.precio - (producto.precio * producto.descuento/100)
    producto.save()
    return redirect(to="home")

def suscribir(request):
    contexto = {'form': SuscripcionForm()}
    if request.method == "POST":
        Suscripcion = SuscripcionForm(request.POST)
        if Suscripcion.is_valid:
            Suscripcion.save()
            contexto["mensaje"] = "Suscripcion Realizada!."
    return render(request, 'core/suscribir.html', contexto)

    
def carrito(request):
    return render(request, "pedido.html")