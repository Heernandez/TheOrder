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
    envio al template los productos para mostrar
    '''
    doc = get_template("menu.html")
    documento = doc.render({"productos":productos})

    return HttpResponse(documento)

def cambiar_estado(request):
    '''
    aqui debo cargar el html para la vista
    de los empleados donde se cambia el 
    estado del pedido de en preparacion a listo
    '''
    return render(request,"preparacion.html")

def visualizar_estado(request):
    '''
    aqui debo cargar el html para la vista
    de los pedidos actuales y el estado
    '''
    return render(request,"entrega.html")