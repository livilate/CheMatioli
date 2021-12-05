from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto

# Create your views here.
def all_products(request):
    productos = Producto.objects.all()
    return render(request, 'main/home.html', {'productos': productos})


def categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}

def detalle_producto(request, id):
    producto = Producto.objects.get(id == id)
    producto = get_object_or_404(Producto, id == id, EnStock=True)
    return render(request, 'main/productos/detail.html', {'producto': producto})