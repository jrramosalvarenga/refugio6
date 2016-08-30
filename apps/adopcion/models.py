from django.db import models


class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=70)
	email = models.EmailField()
	domicilio = models.TextField()

	def __unicode__(self):
		return '{} {}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
	persona=models.ForeignKey(Persona,null=True,blank=True)
	numero_mascotas=models.IntegerField()
	razones=models.TextField()


