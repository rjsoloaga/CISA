from django.db import models

class OpcionesTipoInstituto(models.TextChoices):
    SELECCIONAR = '', 'Selecciona un tipo...'
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    AMBAS = 'A', 'Ambas'
    SACERDOTAL = 'S', 'Sacerdotal'
    LAICAL = 'L', 'Laical'

class Instituto(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Completo del Instituto")
    sigla = models.CharField(max_length=30, null=True, blank=True, verbose_name="Sigla / Acrónimo")
    logo = models.ImageField(upload_to='institutos/logos/', null=True, blank=True, verbose_name="Logo")
    breve_descripcion = models.TextField(null=True, blank=True, verbose_name="Breve Descripción")
    historia = models.TextField(null=True, blank=True, verbose_name="Historia y Hitos de Fundación")
    carisma = models.TextField(null=True, blank=True, verbose_name="Carisma o Espiritualidad")
    
    anio_fundacion = models.TextField(null=True, blank=True, verbose_name="Año / Fechas de Fundación")
    fundador = models.TextField(null=True, blank=True, verbose_name="Fundador/a o Proceso Fundacional")
    foto_fundador = models.ImageField(upload_to='institutos/fundadores/', null=True, blank=True, verbose_name="Foto del Fundador/a")
    pais_origen = models.CharField(max_length=150, null=True, blank=True, verbose_name="País de Origen")

    tipo_instituto = models.CharField(max_length=1, choices=OpcionesTipoInstituto.choices, default=OpcionesTipoInstituto.SELECCIONAR, verbose_name="Tipo de Instituto")
    responsable = models.CharField(max_length=200, null=True, blank=True, verbose_name="Responsable General")
    consejo_gobierno = models.TextField(null=True, blank=True, verbose_name="Consejo o Equipo de Gobierno")
    numero_miembros = models.CharField(max_length=150, null=True, blank=True, verbose_name="Número de Miembros")
    paises_presencia = models.TextField(null=True, blank=True, verbose_name="Países donde está presente")

    anio_llegada_argentina = models.CharField(max_length=100, null=True, blank=True, verbose_name="Año de llegada a Argentina")
    provincias_diocesis = models.TextField(null=True, blank=True, verbose_name="Provincias o Diócesis en Argentina")
    casas_comunidades = models.TextField(null=True, blank=True, verbose_name="Casas, Comunidades u Obras")
    tipo_presencia = models.CharField(max_length=200, null=True, blank=True, verbose_name="Tipo de Presencia")

    direccion = models.TextField(null=True, blank=True, verbose_name="Dirección / Ubicaciones")
    telefono = models.TextField(null=True, blank=True, verbose_name="Teléfonos / Referentes de Contacto")
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Email Oficial")
    website = models.URLField(max_length=500, null=True, blank=True, verbose_name="Sitio Web Oficial")
    redes_sociales = models.TextField(null=True, blank=True, verbose_name="Redes Sociales")

    class Meta:
        verbose_name = "Instituto"
        verbose_name_plural = "Institutos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.sigla})" if self.sigla else self.nombre