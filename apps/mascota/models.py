from django.db import models

from apps.adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)


    def __unicode__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    vacuna = models.CharField
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)





