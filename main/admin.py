from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Slug']
    populated_fields = { 'Slug': ('Nombre',) }

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nombre', 'CreadoPor', 'Precio', 'EnStock', 'FechaCreacion', 'FechaActualizacion', 'Slug']
    list_filter = ['EnStock', 'Activo']
    list_editable = ['Precio', 'EnStock']
    populated_fields = { 'Slug': ('Nombre',) }