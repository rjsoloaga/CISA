from django.db import models

class InformacionInstitucional(models.Model):
    nombre_presidente = models.CharField(
        max_length=150, 
        verbose_name="Nombre del Presidente/a"
    )
    correo = models.EmailField(
        verbose_name="Correo Electrónico de Contacto"
    )
    telefono = models.CharField(
        max_length=50, 
        verbose_name="Teléfono / WhatsApp"
    )
    direccion = models.CharField(
        max_length=255, 
        verbose_name="Dirección Institucional"
    )
    actualizado_el = models.DateTimeField(
        auto_now=True, 
        verbose_name="Última modificación"
    )

    class Meta:
        verbose_name = "Información Institucional"
        verbose_name_plural = "Información Institucional"

    def __str__(self):
        return f"Contacto CISA - Presidencia: {self.nombre_presidente}"