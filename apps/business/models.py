from django.db import models
from apps.projects.models import Project
from apps.persona.models import Persona
# Create your models here.

class Empresa(models.Model):
	nombre = models.CharField(max_length = 50)
	rut = models.CharField(max_length = 12)
	direccion = models.TextField()
	ciudad = models.CharField(max_length = 20)
	telefono = models.CharField(max_length = 12)
	email = models.EmailField()
	proyectos = models.ForeignKey(Project, null = True, blank = True, on_delete = models.CASCADE)
	miembros = models.ForeignKey(Persona, null = True, blank = True, on_delete = models.CASCADE)

