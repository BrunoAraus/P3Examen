from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home,name="home"),
    path('usuario', usuario,name="usuario"),
    path('historial', historial,name="historial"),
    path('pedido', pedido,name="pedido"),
    path('CrearProducto', CrearProducto, name="CrearProducto"),
    path('Gestionar', Gestionar, name="Gestionar"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('producto/<id>', producto, name="producto"),
    path('descontar/<id>', descontar, name="descontar"),
    path('descuento/<id>', descuento, name="descuento"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path('registro', registro,name="registro"),
]