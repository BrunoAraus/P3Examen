from django.urls import URLPattern, path
from rest_suscripcion.views import detalle_sus, lista_sus

urlpatterns = [
    path('lista_sus', lista_sus, name="lista_sus"),
    path('detalle_sus/<id>', detalle_sus, name="detalle_sus"),
]