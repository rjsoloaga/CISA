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
        ('📋 Información Principal', {
            'fields': ('titulo', 'fecha', 'descripcion'),
            'description': 'Campos indispensables para la carga de la asamblea o comunicado.',
        }),
        ('📎 Documentación adjunta', {
            'fields': ('archivo',),
            'description': 'Ayuda: Adjunte el documento en formato PDF.',
        }),
        ('⚙️ Opciones Avanzadas', {
            'fields': ('tipo', 'estado', 'lugar', 'url_externa', 'destacada', 'activo'),
            'classes': ('collapse',),
            'description': 'Metadatos adicionales y configuración de visualización.',
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
