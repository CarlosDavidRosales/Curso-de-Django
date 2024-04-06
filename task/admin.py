from django.contrib import admin
from .models import Tareas


# Register your models here.

class TareasAdmin(admin.ModelAdmin):
    list_display = ('tarea', 'fecha', 'completado', 'user')

admin.site.register(Tareas, TareasAdmin)

