from django.db import models

class Autoridad(models.Model):
    cargo = models.CharField(
        max_length=100, 
        help_text="Ej: Presidente/a, Vicepresidente/a, Secretario/a"
    )
    nombre_completo = models.CharField(
        max_length=150, 
        verbose_name="Nombre y Apellido"
    )
    orden = models.PositiveIntegerField(
        default=0, 
        help_text="Orden de visualización (ej: 1 para Presidente, 2 para Vice, 3 para Secretario)"
    )

    class Meta:
        verbose_name = "Autoridad"
        verbose_name_plural = "Autoridades"
        ordering = ['orden', 'id']

    def __str__(self):
        return f"{self.cargo}: {self.nombre_completo}"