from django.db import models

# Create your models here.

#sse rean como clases que heredan de models.Model 
#y los atributos se especfican con models.(tipodato)Field(....)

class Producto(models.Model):
    idProducto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 30)
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre

class ListaItem(models.Model):
    idPedido = models.IntegerField()
    idProducto = models.CharField(max_length = 30)
    cantidad = models.IntegerField()
    detalle = models.CharField(max_length = 50)

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key = True)
    idEstado = models.IntegerField()
    tipoPedido = models.CharField(max_length = 20)
    total = models.IntegerField()

class Estado(models.Model):
    idEstado = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 30)