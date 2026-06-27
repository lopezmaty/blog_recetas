from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Recetas(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField()
    categorias = models.ManyToManyField(Categorias)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.categorias