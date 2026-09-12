from django.contrib import admin
from django.utils.html import format_html
from .models import Autoridad, Asamblea


# ══════════════════════════════════════════════════════════
# AUTORIDADES (uso interno)
# ══════════════════════════════════════════════════════════

@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
    list_display  = ('cargo', 'nombre_completo', 'orden')
    list_editable = ('orden',)
    search_fields = ('cargo', 'nombre_completo')
    ordering      = ('orden', 'id')

    fieldsets = (
        ('👤 Datos de la Autoridad', {
            'fields': ('cargo', 'nombre_completo', 'orden'),
            'description': (
                'Registre los cargos y nombres de la Comisión Directiva de CISA. '
                'El campo "Orden" determina el orden de aparición (1 = primer puesto).'
            ),
        }),
    )


# ══════════════════════════════════════════════════════════
# ASAMBLEAS (vista pública)
# ══════════════════════════════════════════════════════════

@admin.register(Asamblea)
class AsambleaAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'tipo', 'estado_badge', 'fecha', 'lugar', 'destacada', 'activo')
    list_filter   = ('tipo', 'estado', 'destacada', 'activo')
    list_editable = ('destacada', 'activo')
    search_fields = ('titulo', 'descripcion', 'lugar')
    ordering      = ('-fecha', 'orden')
    date_hierarchy = 'fecha'

    fieldsets = (
        ('📋 Información de la Asamblea', {
            'fields': ('tipo', 'estado', 'titulo', 'fecha', 'lugar', 'descripcion'),
            'description': (
                'Complete el tipo (Convocatoria, Informe o Comunicado), el estado actual, '
                'el título oficial, la fecha y el lugar o modalidad de la asamblea.'
            ),
        }),
        ('📎 Documentación adjunta', {
            'fields': ('archivo', 'url_externa'),
            'classes': ('collapse',),
            'description': (
                'Adjunte el documento PDF de convocatoria o acta, O ingrese una URL externa. '
                'No es necesario completar ambos campos.'
            ),
        }),
        ('⚙️ Configuración de Visualización', {
            'fields': ('destacada', 'activo', 'orden'),
            'description': (
                '"Destacada" muestra la asamblea en posición prioritaria. '
                '"Visible en el sitio" controla si aparece públicamente.'
            ),
        }),
    )

    @admin.display(description='Estado', ordering='estado')
    def estado_badge(self, obj):
        estilos = {
            'proxima':   ('background:#228BE6;', 'Próxima'),
            'realizada': ('background:#28A745;', 'Realizada'),
            'cancelada': ('background:#DC3545;', 'Cancelada'),
        }
        estilo, label = estilos.get(obj.estado, ('background:#888;', obj.estado))
        return format_html(
            '<span style="{}color:#fff;padding:2px 10px;border-radius:20px;font-size:0.8rem;">{}</span>',
            estilo, label
        )
