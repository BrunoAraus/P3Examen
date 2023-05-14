from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','stock','categoria','imagen']

class ProductoForm2(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','stock','descuento','precio_final','categoria','imagen']






# class SuscripcionForm(ModelForm):
#     class Meta:
#         model = Suscripciones
#         fields = ['codigo','usuario','estado']