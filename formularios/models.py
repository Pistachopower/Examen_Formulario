from django.db import models
from django.utils import timezone

class Usuario(models.Model):    
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    puede_tener_promociones = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Promociones(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion= models.CharField(max_length=100, default= 'vacio')
    descuento= models.FloatField(default=0.0,db_column = "Descuento")
    codigo = models.IntegerField(null = True)
    fecha_Inicio_Promocion = models.DateTimeField(default=timezone.now)
    fecha_Fin_Promocion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_promociones")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="producto_promociones")

    def __str__(self):
        return self.nombre