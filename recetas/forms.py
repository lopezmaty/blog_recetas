from . import models
from django.forms import ModelForm

class RecetaForm(ModelForm):
    class Meta:
        model = models.Recetas
        fields = ['titulo', 'descripcion', 'imagen', 'categorias']