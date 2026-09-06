from .models import InformacionInstitucional

def contacto_institucional(request):
    return {
        'institucional_global': InformacionInstitucional.objects.first()
    }