from django.contrib import admin
from django.urls import path

import carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', carrito, name="Carrito")
]
