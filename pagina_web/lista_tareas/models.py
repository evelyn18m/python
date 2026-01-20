from django.db import models

# Create your models here.
class Tarea(models.Model):
    ESTADOS=(
        ('1','Pendiente'),
        ('2','En_progreso'),
        ('3','Completado'),
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.IntegerField(default=0)
    fecha_creacion = models.DateField(auto_now_add=True)