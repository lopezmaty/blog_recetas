from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.urls import reverse_lazy

# Create your views here.

class RecetasListView(ListView):
    template_name = 'recetas/lista_recetas.html'
    model = models.Recetas
    context_object_name = 'recetas'


class RecetasDetailView(DetailView):
    template_name = 'recetas/detalle_recetas.html'
    model = models.Recetas
    context_object_name = 'receta'
    

class RecetasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recetas/crear_recetas.html'
    model = models.Recetas
    form_class = forms.RecetaForm
    success_url = reverse_lazy('recetas:lista')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class RecetasUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'recetas/editar_recetas.html'
    model = models.Recetas
    form_class = forms.RecetaForm
    success_url = reverse_lazy('recetas:lista')


class RecetasDeleteView(LoginRequiredMixin, DeleteView):  
    template_name = 'recetas/eliminar_recetas.html'  
    model = models.Recetas
    success_url = reverse_lazy('recetas:lista')