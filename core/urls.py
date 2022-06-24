from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home,name="home"),
    path('usuario', usuario,name="usuario"),
    path('historial', historial,name="historial"),
    path('pedido', pedido,name="pedido"),
    path('CrearPlato', CrearPlato, name="CrearPlato"),
    path('Gestionar', Gestionar, name="Gestionar"),
    path('eliminarPlato/<id>', eliminarPlato, name="eliminarPlato"),
    path('modificarPlato/<id>', modificarPlato, name="modificarPlato"),
    path('producto/<id>', producto, name="producto"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path('registro', registro,name="registro"),
]