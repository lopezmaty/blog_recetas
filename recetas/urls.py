from django.urls import path,  include
from . import views


app_name = 'recetas'

urlpatterns = [
    path('lista/', views.RecetasListView.as_view(), name='lista'),
    path('detalle/<int:pk>/', views.RecetasDetailView.as_view(), name='detalle'),
    path('crear/', views.RecetasCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', views.RecetasUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', views.RecetasDeleteView.as_view(), name='eliminar'),

]

