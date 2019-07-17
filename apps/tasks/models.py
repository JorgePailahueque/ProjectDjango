from django.db import models
from apps.persona.models import Persona
# Create your models here.
# recursos
class Resource(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

#  0 - 25 - 50 - 75 - 100  (%)
class Status(models.Model): 
    id = models.CharField(max_length=3, primary_key=True)
    percent = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.percent, ' %')

class Task(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    des = models.CharField(max_length=200)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    asignado = models.ManyToManyField(Persona)
    status = models.ManyToManyField(Status)
    resources = models.ManyToManyField(Resource, blank=True)