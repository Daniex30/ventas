from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(
        max_length=30
    ) 

    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    nombre = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    unidad_medida = models.CharField(max_length=10)
    precio_venta = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE )
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo + ' ' + self.nombre + ' ' + self.descripcion + ' ' + self.unidad_medida + ' ' + str(self.precio_venta)
    
    def get_categoria(self):
        return self.categoria
    
    def get_marca(self):
        return self.marca
    
    def get_estado(self):
        return self.estado
