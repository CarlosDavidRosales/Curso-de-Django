from django.forms import ModelForm
from .models import Tareas

class TareasForm(ModelForm):
    class Meta:
        model = Tareas
        fields = ['tarea', 'fecha', 'completado']