from django.db import models
from apps.tasks.models import Task
from apps.persona.models import Persona

# Create your models here.

class Project(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    tasks = models.ManyToManyField(Task)
    participantes = models.ManyToManyField(Persona)
    
    def __str__(self):
	    return '{}'.format(self.nombre)
