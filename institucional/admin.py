from django.contrib import admin
from .models import InformacionInstitucional

@admin.register(InformacionInstitucional)
class InformacionInstitucionalAdmin(admin.ModelAdmin):
    list_display = ('nombre_presidente', 'correo', 'telefono', 'actualizado_el')