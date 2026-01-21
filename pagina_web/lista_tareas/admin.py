from django.contrib import admin

from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','estado')
    search_fields = ('titulo','descripcion')
    list_filter = ('estado',)

# Register your models here.
admin.site.register(Tarea, TareaAdmin)