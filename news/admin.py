from django.contrib import admin
from django.utils.html import format_html
from .models import news, InformacionContacto, RedSocial, DatoContactoAdicional, Documento


# ══════════════════════════════════════════════════════════
# NOTICIAS
# ══════════════════════════════════════════════════════════

@admin.register(news)
class NoticiaAdmin(admin.ModelAdmin):
    list_display   = ('titulo', 'fecha', 'fecha_evento', 'ubicacion')
    list_filter    = ('fecha', 'fecha_evento')
    search_fields  = ('titulo', 'resumen', 'cuerpo', 'ubicacion')
    ordering       = ('-fecha',)
    date_hierarchy = 'fecha'

    fieldsets = (
        ('📝 Contenido de la Noticia', {
            'fields': ('titulo', 'resumen', 'cuerpo', 'imagen'),
            'description': 'Escriba el título, el resumen (texto breve) y el contenido completo de la noticia. La imagen es opcional.',
        }),
        ('📅 Datos del Evento (opcional)', {
            'fields': ('fecha_evento', 'hora_evento', 'ubicacion'),
            'classes': ('collapse',),
            'description': 'Complete esta sección solo si la noticia hace referencia a un evento con fecha y lugar específicos.',
        }),
    )


# ══════════════════════════════════════════════════════════
# INFORMACIÓN DE CONTACTO (Singleton — un único registro)
# ══════════════════════════════════════════════════════════

@admin.register(InformacionContacto)
class InformacionContactoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('📬 Datos de Contacto Principal', {
            'fields': ('correo', 'telefono', 'whatsapp', 'horario_atencion'),
            'description': (
                '⚠️ Estos datos aparecen en el pie de página y en la página de Contacto del sitio. '
                'Solo debe existir UN registro. No agregue un segundo registro.'
            ),
        }),
        ('📍 Ubicación', {
            'fields': ('direccion',),
        }),
    )

    def has_add_permission(self, request):
        """Bloquea la creación de un segundo registro (patrón singleton)."""
        return not InformacionContacto.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Impide borrar el único registro de contacto."""
        return False


# ══════════════════════════════════════════════════════════
# REDES SOCIALES
# ══════════════════════════════════════════════════════════

@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'url', 'orden')
    list_editable = ('orden',)
    ordering      = ('orden', 'nombre')

    fieldsets = (
        ('🌐 Red Social', {
            'fields': ('nombre', 'icono', 'url', 'orden'),
            'description': 'Agregue o modifique los perfiles de redes sociales de CISA que aparecen en el pie de página.',
        }),
    )


# ══════════════════════════════════════════════════════════
# DATOS DE CONTACTO ADICIONALES
# ══════════════════════════════════════════════════════════

@admin.register(DatoContactoAdicional)
class DatoContactoAdicionalAdmin(admin.ModelAdmin):
    list_display  = ('etiqueta', 'tipo', 'valor', 'orden')
    list_editable = ('orden',)
    list_filter   = ('tipo',)
    ordering      = ('orden', 'etiqueta')

    fieldsets = (
        ('➕ Dato Adicional de Contacto', {
            'fields': ('etiqueta', 'valor', 'tipo', 'icono', 'orden'),
            'description': (
                'Use esta sección para agregar datos extra de contacto como una sede secundaria, '
                'un correo alternativo, un teléfono de guardia, etc.'
            ),
        }),
    )


# ══════════════════════════════════════════════════════════
# DOCUMENTOS INSTITUCIONALES
# ══════════════════════════════════════════════════════════

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'categoria_badge', 'formato', 'activo', 'orden')
    list_filter   = ('categoria', 'formato', 'activo')
    list_editable = ('activo', 'orden')
    search_fields = ('titulo', 'subtitulo', 'descripcion', 'referencia')
    ordering      = ('categoria', 'orden', 'titulo')

    fieldsets = (
        ('📄 Identificación del Documento', {
            'fields': ('categoria', 'titulo', 'subtitulo', 'referencia'),
            'description': 'Ingrese la categoría, el título oficial y la referencia canónica o año del documento.',
        }),
        ('📝 Descripción', {
            'fields': ('descripcion',),
            'classes': ('collapse',),
            'description': 'Descripción ampliada del documento, su historia e importancia doctrinal (opcional).',
        }),
        ('📎 Archivo o Enlace', {
            'fields': ('formato', 'archivo', 'url_externa'),
            'description': (
                'Suba el archivo PDF/DOCX en "Archivo", O ingrese una URL en "Enlace externo". '
                'No complete ambos campos al mismo tiempo.'
            ),
        }),
        ('⚙️ Configuración de Visualización', {
            'fields': ('activo', 'orden'),
            'description': '"Visible en el sitio" controla si aparece en la web. "Orden" define la posición dentro de la categoría.',
        }),
    )

    @admin.display(description='Categoría', ordering='categoria')
    def categoria_badge(self, obj):
        colores = {
            'folletos_cisa':      '#228BE6',
            'documentos_iglesia': '#18314F',
        }
        color = colores.get(obj.categoria, '#888')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 10px;border-radius:20px;font-size:0.8rem;">{}</span>',
            color, obj.get_categoria_display()
        )
