from news.models import InformacionContacto, RedSocial

def datos_contacto_global(request):
    try:
        contacto = InformacionContacto.get_solo()
        redes = RedSocial.objects.all()
    except Exception:
        contacto = None
        redes = []
    
    return {
        'institucional_global': contacto,
        'redes_globales': redes
    }