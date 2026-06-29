from django.db.models import DateTimeField
from django.db import models

# Create your models here.

class news(models.Model):

    titulo = models.CharField(max_length=50)
    resumen = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    cuerpo = models.TextField()
    ubicacion = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ubicación")
    fecha_evento = models.DateField(blank=True, null=True, verbose_name="Fecha del Evento")
    hora_evento = models.TimeField(blank=True, null=True, verbose_name="Hora del Evento")

    def __str__(self):
        return self.titulo