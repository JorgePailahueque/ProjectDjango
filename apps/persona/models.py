from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 70)
	rut = models.CharField(max_length = 12)
	telefono = models.CharField(max_length = 12)
	email = models.EmailField()
	domicilio = models.TextField()
	fecha_ingreso = models.DateField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)