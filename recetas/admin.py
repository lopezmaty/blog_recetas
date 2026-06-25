from django.contrib import admin
from . import models

# Register your models here.



@admin.register(models.Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    fields = ('nombre',)

@admin.register(models.Recetas)
class RecetasAdmin(admin.ModelAdmin):
    fields = ('titulo', 'descripcion', 'imagen', 'categorias', 'autor', 'fecha_hora')
    list_filter = ('categorias', 'autor',)
    search_fields = ('titulo',)
    

