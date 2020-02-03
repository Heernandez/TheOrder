from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

# Se crean como funciones, reciben el request y 
# retornan un render y la plantilla html

from gestionPedido.models import Producto, Pedido, ListaItem , Estado

def hacer_pedido(request):

    productos = Producto.objects.all() 
    '''
    envio al template la lista de productos para su visualizacion 
    
    '''
    doc = get_template("menu.html")
    documento = doc.render({"productos":productos})

    return HttpResponse(documento)

def cambiar_estado(request):
    pedidos = Pedido.objects.all()
    '''
    Envio al template la lista de pedidos en orden 
    para que a traves del mismo 
    los empleados monitoreen y modifiquen el estado del pedido
    
    '''
    return render(request,"preparacion.html")

def visualizar_estado(request):
    lista = Pedido.objects.all()
    '''
    Envio los pedidos actuales al template para que
    este los muestre con su estado actual para que 
    los clientes monitoreen su estado
    '''
    return render(request,"entrega.html")