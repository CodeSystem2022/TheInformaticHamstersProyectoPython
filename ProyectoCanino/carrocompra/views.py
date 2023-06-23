from django.shortcuts import render
from .carrocompra import CarroCompra
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

#Funcion que agrega productos al carro
def agregar_productos(request, producto_id):
    #Instancia de la clase CarroCompra, se crea cada vez que armamos un carro de compra
    carro = CarroCompra(request)
    #Obtenemos el producto que vamos a agregar al carro
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")

#Funcion para eliminar productos del carro
def eliminar_productos(request, producto_id):
    carro = CarroCompra(request)
    #Obtenemos el producto que vamos a eliminar al carro
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

#Funcion que restar productos al carro
def restar_productos(request, producto_id):
    carro = CarroCompra(request)
    #Obtenemos el producto que vamos a restar al carro
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

#Funcion que limpiar  productos al carro
def limpiar_productos(request, producto_id):
    carro = CarroCompra(request)
    carro.limpiar_carro()
    return redirect("Tienda")