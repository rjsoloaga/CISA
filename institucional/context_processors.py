def contacto_institucional(request):
    """Inyecta en todos los templates los datos de contacto institucional globales."""
    try:
        from news.models import InformacionContacto, RedSocial
        contacto = InformacionContacto.get_solo()
        redes = list(RedSocial.objects.all().order_by('orden', 'nombre'))
    except Exception:
        contacto = None
        redes = []
    return {
        'institucional_global': contacto,
        'redes_globales': redes,
    }


def datos_institucionales(request):
    """Alias de compatibilidad (no registrado en settings, puede quedar vacío)."""
    return {}