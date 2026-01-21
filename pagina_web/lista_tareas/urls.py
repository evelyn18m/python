from django.urls import path
from .views import ListaTareas, ListaTareasCrear, ListaTareasDetalle, ListaTareasEditar, ListaTareasEliminar

urlpatterns = [
    path('', ListaTareas.as_view(), name='lista_tareas'),
    path('crear/', ListaTareasCrear.as_view(), name='crear_tareas'),
    path('<int:pk>', ListaTareasDetalle.as_view(), name='detalle_tarea'),
    path('editar/<int:pk>', ListaTareasEditar.as_view(), name='editar_tarea'),
    path('eliminar/<int:pk>', ListaTareasEliminar.as_view(), name='eliminar_tarea'),
]