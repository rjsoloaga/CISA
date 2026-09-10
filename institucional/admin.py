from django.contrib import admin
from .models import Autoridad

@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'nombre_completo', 'orden')
    list_editable = ('orden',)
    search_fields = ('cargo', 'nombre_completo')