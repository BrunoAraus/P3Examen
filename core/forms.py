from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','stock','descuento','precio_final','categoria','imagen']