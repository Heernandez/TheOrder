from django.contrib import admin

# Register your models here.

from gestionPedido.models import Pedido,Producto,ListaItem,Estado
#se importan los modelos gestionpedido. y la clase a importar
# y se registran con admin.site.register()...

admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(ListaItem)
admin.site.register(Estado)