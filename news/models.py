from django.db import models

# ==========================================
# MODELO DE NOTICIAS
# ==========================================

class news(models.Model):
    titulo = models.CharField(
        max_length=50,
        verbose_name="Título",
        help_text="Título breve de la noticia (máx. 50 caracteres)."
    )
    resumen = models.TextField(
        verbose_name="Resumen",
        help_text="Texto corto que aparece en la tarjeta de la noticia (1-2 oraciones)."
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    imagen = models.ImageField(
        upload_to='noticias/',
        null=True, blank=True,
        verbose_name="Imagen",
        help_text="Imagen principal. Formatos: JPG, PNG, WEBP. Tamaño recomendado: 1200×630 px."
    )
    cuerpo = models.TextField(
        verbose_name="Contenido completo",
        help_text="Desarrollo completo de la noticia. Puede incluir párrafos, listas, etc."
    )
    ubicacion = models.CharField(
        max_length=200, blank=True, null=True,
        verbose_name="Ubicación",
        help_text="Lugar donde se realizará o realizó el evento (ej: 'Sede Central, Salón A')."
    )
    fecha_evento = models.DateField(
        blank=True, null=True,
        verbose_name="Fecha del Evento",
        help_text="Fecha del evento al que hace referencia la noticia (distinta de la fecha de publicación)."
    )
    hora_evento = models.TimeField(
        blank=True, null=True,
        verbose_name="Hora del Evento",
        help_text="Hora de inicio del evento en formato HH:MM."
    )

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


# ==========================================
# INFORMACIÓN PRINCIPAL DE CONTACTO (SINGLETON)
# ==========================================

class InformacionContacto(models.Model):
    correo = models.EmailField(
        blank=True, null=True,
        verbose_name="Correo Electrónico",
        help_text="Dirección de correo institucional principal (ej: contacto@cisa.org.ar)."
    )
    direccion = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name="Dirección Central",
        help_text="Dirección postal completa de la sede central (ej: Av. General Paz 1234, CABA)."
    )
    telefono = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="Teléfono Fijo",
        help_text="Número de teléfono fijo con código de área (ej: +54 (11) 4567-8901)."
    )
    whatsapp = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="WhatsApp Oficial",
        help_text="Número de WhatsApp con código de país y área, sin espacios ni guiones (ej: +5491145678901). Se usará para generar el enlace de chat directo."
    )
    horario_atencion = models.CharField(
        max_length=150, blank=True, null=True,
        verbose_name="Horario de Atención",
        help_text="Horarios en los que se puede contactar (ej: Lunes a Viernes de 9:00 a 18:00 hs.)."
    )

    class Meta:
        verbose_name = "⚙️ Información de Contacto"
        verbose_name_plural = "⚙️ Información de Contacto"

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


# ==========================================
# DOCUMENTOS INSTITUCIONALES
# ==========================================

class Documento(models.Model):
    CATEGORIA_CHOICES = [
        ('folletos_cisa',      'Folletos CEDIS / CISA'),
        ('documentos_iglesia', 'Documentos de la Iglesia'),
    ]
    FORMATO_CHOICES = [
        ('pdf',    'PDF'),
        ('enlace', 'Enlace externo'),
        ('docx',   'DOCX / Word'),
    ]

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIA_CHOICES,
        verbose_name="Categoría",
        help_text="Bloque de la página donde aparecerá este documento."
    )
    titulo = models.CharField(
        max_length=300,
        verbose_name="Título oficial",
        help_text="Nombre completo y oficial del documento (ej: 'Constitución Apostólica Provida Mater Ecclesia')."
    )
    subtitulo = models.CharField(
        max_length=300, blank=True,
        verbose_name="Subtítulo / Contexto",
        help_text="Breve descripción complementaria del documento (ej: 'Primer documento pontificio sobre los Institutos Seculares')."
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción",
        help_text="Explicación del documento, su importancia y contexto histórico-doctrinal."
    )
    referencia = models.CharField(
        max_length=200, blank=True,
        verbose_name="Referencia canónica / Año",
        help_text="Año de promulgación, número de canon u otra referencia oficial (ej: '2 de febrero de 1947 · Pío XII')."
    )
    formato = models.CharField(
        max_length=10,
        choices=FORMATO_CHOICES,
        default='pdf',
        verbose_name="Formato",
        help_text="Tipo de recurso que se vinculará (PDF descargable, enlace externo o documento Word)."
    )
    archivo = models.FileField(
        upload_to='documentos/',
        null=True, blank=True,
        verbose_name="Archivo (PDF / DOCX)",
        help_text="Suba aquí el archivo del documento. Solo si no usa 'Enlace externo'."
    )
    url_externa = models.URLField(
        blank=True,
        verbose_name="Enlace externo (URL)",
        help_text="URL de lectura en línea si no sube un archivo local (ej: https://www.vatican.va/...). Completar uno u otro, no ambos."
    )
    orden = models.PositiveIntegerField(
        default=1,
        verbose_name="Orden",
        help_text="Número de posición dentro de la categoría (1 = primero)."
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Visible en el sitio",
        help_text="Desmarque para ocultar este documento del sitio sin eliminarlo."
    )

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ['categoria', 'orden', 'titulo']

    def __str__(self):
        return f"[{self.get_categoria_display()}] {self.titulo}"

    @property
    def link_descarga(self):
        """Devuelve la URL de descarga/lectura, priorizando archivo local."""
        if self.archivo:
            return self.archivo.url
        return self.url_externa or None