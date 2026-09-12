from django.db import models


# ==========================================
# AUTORIDADES DE CISA (uso interno / Admin)
# ==========================================

class Autoridad(models.Model):
    cargo = models.CharField(
        max_length=100,
        verbose_name="Cargo",
        help_text="Ej: Presidente/a, Vicepresidente/a, Secretario/a General."
    )
    nombre_completo = models.CharField(
        max_length=150,
        verbose_name="Nombre y Apellido",
        help_text="Nombre y apellido completos de la persona que ocupa el cargo."
    )
    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden de visualización",
        help_text="Número de posición en la lista (ej: 1 para Presidente, 2 para Vice, 3 para Secretario)."
    )

    class Meta:
        verbose_name = "Autoridad"
        verbose_name_plural = "Autoridades"
        ordering = ['orden', 'id']

    def __str__(self):
        return f"{self.cargo}: {self.nombre_completo}"


# ==========================================
# ASAMBLEAS (vista pública: convocatorias,
# informes y comunicados)
# ==========================================

class Asamblea(models.Model):
    TIPO_CHOICES = [
        ('convocatoria', 'Convocatoria'),
        ('informe',      'Informe / Acta'),
        ('comunicado',   'Comunicado'),
    ]
    ESTADO_CHOICES = [
        ('proxima',   'Próxima'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='convocatoria',
        verbose_name="Tipo de publicación",
        help_text="Seleccione si es una convocatoria previa, un informe posterior o un comunicado general."
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='proxima',
        verbose_name="Estado",
        help_text="Estado actual de la asamblea: 'Próxima' para futuras, 'Realizada' para ya celebradas."
    )
    titulo = models.CharField(
        max_length=300,
        verbose_name="Título",
        help_text="Nombre oficial de la asamblea (ej: 'Asamblea Ordinaria CISA 2025 — Primer Semestre')."
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción / Temario",
        help_text="Detalles, temario, resoluciones o resumen de lo tratado en la asamblea."
    )
    fecha = models.DateField(
        verbose_name="Fecha",
        help_text="Fecha de realización de la asamblea (o fecha estimada si es próxima)."
    )
    lugar = models.CharField(
        max_length=200, blank=True,
        verbose_name="Lugar / Modalidad",
        help_text="Lugar físico o modalidad (ej: 'Sede Central, Buenos Aires' o 'Virtual — Zoom')."
    )
    archivo = models.FileField(
        upload_to='asambleas/',
        null=True, blank=True,
        verbose_name="Documento adjunto (PDF)",
        help_text="Suba el acta, convocatoria formal u otro documento en PDF."
    )
    url_externa = models.URLField(
        blank=True,
        verbose_name="Enlace externo (URL)",
        help_text="URL alternativa si el documento está alojado en otro sitio. Use solo si no adjunta archivo."
    )
    destacada = models.BooleanField(
        default=False,
        verbose_name="Destacada",
        help_text="Marque para resaltar esta asamblea en la parte superior de la página."
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Visible en el sitio",
        help_text="Desmarque para ocultar esta entrada sin eliminarla."
    )
    orden = models.PositiveIntegerField(
        default=1,
        verbose_name="Orden manual",
        help_text="Número de prioridad cuando dos asambleas tienen la misma fecha (1 = mayor prioridad)."
    )

    class Meta:
        verbose_name = "Asamblea"
        verbose_name_plural = "Asambleas"
        ordering = ['-fecha', 'orden']

    def __str__(self):
        return f"{self.get_tipo_display()} — {self.titulo} ({self.fecha})"

    @property
    def link_documento(self):
        """Devuelve la URL del documento, priorizando archivo local."""
        if self.archivo:
            return self.archivo.url
        return self.url_externa or None