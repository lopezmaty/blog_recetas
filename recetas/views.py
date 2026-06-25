from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RecetasListView(ListView):
    template_name = 'recetas/lista_recetas.html'
    model = models.Recetas
    context_object_name = 'recetas'


class RecetasDetailView(DetailView):
    template_name = 'recetas/detalle_recetas.html'
    model = models.Recetas
    

class RecetasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recetas/crear_recetas.html'
    model = models.Recetas
    fields = ('titulo', 'descripcion', 'imagen', 'categorias',)
    success_url = 'recetas/lista_recetas.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class RecetasUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'recetas/editar_recetas.html'
    model = models.Recetas
    fields = ('titulo', 'descripcion', 'imagen', 'categorias',)
    success_url = 'recetas/lista_recetas.html'


class RecetasDeleteView(LoginRequiredMixin, DeleteView):  
    template_name = 'recetas/eliminar_recetas.html'  
    model = models.Recetas
    success_url = 'recetas/lista_recetas.html'