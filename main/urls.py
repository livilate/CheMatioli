from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.all_products, name='todos_productos'),
    path('producto/<int:id>/', views.detalle_producto, name='producto_detalle')
]