from django.db import models

class OpcionesRama(models.TextChoices):
    SELECCIONAR = '', 'Selecciona una rama...'
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    AMBAS = 'A', 'Ambas'

class Instituto(models.Model):

    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='institutos/', null=True, blank=True)
    responsable = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    fundador = models.TextField()
    carisma = models.TextField()
    rama = models.CharField(max_length=1, choices=OpcionesRama.choices)#, default=OpcionesRama.MASCULINO)