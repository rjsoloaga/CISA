from django.db import models

# ==========================================
# MODELO DE NOTICIAS
# ==========================================

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


# ==========================================
# INFORMACIÓN PRINCIPAL DE CONTACTO (SINGLETON)
# ==========================================

class InformacionContacto(models.Model):
    correo = models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección Central")
    telefono = models.CharField(max_length=50, blank=True, null=True, verbose_name="Teléfono")
    whatsapp = models.CharField(max_length=50, blank=True, null=True, verbose_name="WhatsApp Oficial")
    horario_atencion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Horario de Atención")

    class Meta:
        verbose_name = "Información de Contacto"
        verbose_name_plural = "Información de Contacto"

    def __str__(self):
        return f"Contacto CISA ({self.correo or 'Sin correo'})"

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj

    @property
    def whatsapp_link(self):
        if not self.whatsapp:
            return None
        solo_numeros = ''.join(c for c in self.whatsapp if c.isdigit())
        return f"https://wa.me/{solo_numeros}?text=Hola!%20Me%20comunico%20desde%20la%20web%20de%20CISA"


# ==========================================
# REDES SOCIALES
# ==========================================

class RedSocial(models.Model):
    ICONOS_CHOICES = [
        ('bi-facebook', 'Facebook'),
        ('bi-instagram', 'Instagram'),
        ('bi-twitter-x', 'X (Twitter)'),
        ('bi-youtube', 'YouTube'),
        ('bi-globe', 'Sitio Web / Enlace Genérico'),
    ]

    nombre = models.CharField(max_length=50, help_text="Ej: Instagram Oficial")
    url = models.URLField(verbose_name="Enlace URL")
    icono = models.CharField(max_length=50, choices=ICONOS_CHOICES, default='bi-globe', help_text="Ícono representativo")
    orden = models.PositiveIntegerField(default=1, help_text="Orden de aparición")

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"

    def __str__(self):
        return self.nombre


# ==========================================
# CAMPOS ADICIONALES DE CONTACTO
# ==========================================

class DatoContactoAdicional(models.Model):
    TIPO_CHOICES = [
        ('texto', 'Texto / Dirección'),
        ('correo', 'Correo Electrónico (Enlace directo)'),
        ('telefono', 'Teléfono / Móvil'),
        ('enlace', 'Enlace Web'),
    ]

    ICONOS_CHOICES = [
        ('bi-geo-alt-fill', '📍 Dirección / Ubicación'),
        ('bi-envelope-fill', '✉️ Correo Electrónico'),
        ('bi-telephone-fill', '📞 Teléfono'),
        ('bi-clock-fill', '⏰ Horario'),
        ('bi-globe', '🌐 Sitio Web / Link'),
        ('bi-info-circle-fill', 'ℹ️ Información General'),
    ]

    etiqueta = models.CharField(max_length=60, verbose_name="Nombre del Campo (Ej: Sede Anexo, Teléfono de Guardia)")
    valor = models.CharField(max_length=255, verbose_name="Dato / Contenido")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='texto', verbose_name="Tipo de Dato")
    icono = models.CharField(max_length=50, choices=ICONOS_CHOICES, default='bi-info-circle-fill', verbose_name="Ícono")
    orden = models.PositiveIntegerField(default=1, verbose_name="Orden de aparición")

    class Meta:
        ordering = ['orden', 'etiqueta']
        verbose_name = "Dato de Contacto Adicional"
        verbose_name_plural = "Datos de Contacto Adicionales"

    def __str__(self):
        return f"{self.etiqueta}: {self.valor}"