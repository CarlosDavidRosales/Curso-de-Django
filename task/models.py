from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tareas(models.Model):
    tarea = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    completado = models.BooleanField(default=False)
    # No hacer nada con las tareas si el usuario es eliminado
    user = models.ForeignKey(User, on_delete=models.CASCADE)
