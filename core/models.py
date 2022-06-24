from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCategoria

class Plato(models.Model):
    nombre = models.CharField(primary_key=True, max_length=30)
    precio = models.IntegerField()
    descuento = models.IntegerField(null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.CharField(null=True, max_length=400,blank=True)

    def __str__(self) -> str:
        return self.nombre




    