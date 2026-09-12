from django.contrib import admin
from django.utils.html import format_html
from .models import Instituto


@admin.register(Instituto)
class InstitutoAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'sigla', 'tipo_instituto', 'pais_origen', 'logo_preview')
    list_filter   = ('tipo_instituto', 'pais_origen')
    search_fields = ('nombre', 'sigla', 'responsable', 'email')
    ordering      = ('nombre',)

    fieldsets = (
        ('🏛️ Identidad del Instituto', {
            'fields': ('nombre', 'sigla', 'logo', 'breve_descripcion', 'carisma'),
            'description': (
                'Información principal del instituto. El "Logo" debe ser PNG o JPG con fondo blanco o transparente, '
                'tamaño recomendado: 400×400 px. La "Sigla" es el acrónimo (ej: OFS, FMDJ).'
            ),
        }),
        ('📜 Fundación e Historia', {
            'fields': ('anio_fundacion', 'fundador', 'foto_fundador', 'pais_origen', 'historia'),
            'classes': ('collapse',),
            'description': 'Datos históricos sobre los orígenes del instituto. Todos los campos son opcionales.',
        }),
        ('👥 Gobierno y Estructura', {
            'fields': ('tipo_instituto', 'responsable', 'consejo_gobierno', 'numero_miembros', 'paises_presencia'),
            'classes': ('collapse',),
            'description': (
                '"Tipo de Instituto": Masculino, Femenino, Ambas, Sacerdotal o Laical. '
                '"Responsable General": nombre de quien encabeza el gobierno del instituto actualmente.'
            ),
        }),
        ('🇦🇷 Presencia en Argentina', {
            'fields': ('anio_llegada_argentina', 'provincias_diocesis', 'casas_comunidades', 'tipo_presencia'),
            'classes': ('collapse',),
            'description': 'Datos específicos de la radicación y presencia del instituto en el territorio argentino.',
        }),
        ('📞 Datos de Contacto', {
            'fields': ('direccion', 'telefono', 'email', 'website', 'redes_sociales'),
            'classes': ('collapse',),
            'description': 'Correo electrónico, teléfono, sitio web oficial y redes sociales del instituto.',
        }),
    )

    @admin.display(description='Logo')
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height:40px;width:auto;object-fit:contain;border-radius:4px;" />',
                obj.logo.url
            )
        return '—'
