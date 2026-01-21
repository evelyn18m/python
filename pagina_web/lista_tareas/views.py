from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Tarea
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class ListaTareas(ListView):
    model = Tarea
    template_name = 'lista_tareas/lista.html'
    context_object_name = 'tareas'

class ListaTareasDetalle(DetailView):
    model = Tarea
    template_name = 'lista_tareas/detalles.html'
    context_object_name = 'tarea'
    fields = '__all__'

class ListaTareasCrear(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion']
    template_name = 'lista_tareas/crear.html'
    success_url = reverse_lazy('lista_tareas')

    def get_initial(self):
        initial = super().get_initial()
        initial['estado'] = 1
        return initial

class ListaTareasEditar(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'estado']
    template_name = 'lista_tareas/editar.html'

    def get_success_url(self):
        return reverse_lazy('detalle_tarea', kwargs={'pk': self.object.pk})

class ListaTareasEliminar(DeleteView):
    model = Tarea
    success_url = reverse_lazy('lista_tareas')