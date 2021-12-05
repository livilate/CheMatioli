from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    Nombre = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=10)
    Slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        verbose_name_plural = "categorias"

    def __str__(self) -> str:
        return self.Nombre


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255, db_index=True)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    EnStock = models.BooleanField(default=True)
    Activo = models.BooleanField(default=True)
    Slug = models.SlugField(max_length=255)
    Categoria = models.ForeignKey(Categoria, related_name="producto", on_delete=models.CASCADE)
    Foto = models.ImageField(upload_to="images/")
    CreadoPor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creador_producto")
    Descripcion = models.TextField(blank=True)
    FechaCreacion = models.DateField(auto_now_add=True)
    FechaActualizacion = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "productos"
        ordering = ['-FechaCreacion']

    def get_absolute_url(self):
        return reverse("producto_detalle", kwargs={"pk": self.id})
    

    def __str__(self) -> str:
        return self.Nombre