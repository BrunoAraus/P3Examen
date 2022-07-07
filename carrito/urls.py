from django.contrib import admin
from django.urls import path

import carrito
from core.views import agregar_prducto, eliminar_producto, limpiar_carrito, restar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', carrito, name="Carrito"),
    path('agregar/<int:producto_id>/', agregar_prducto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    
]
