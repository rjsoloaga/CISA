from django import forms
from .models import Autoridad

class AutoridadForm(forms.ModelForm):
    class Meta:
        model = Autoridad
        fields = ['cargo', 'nombre_completo', 'orden']
        labels = {
            'cargo': 'Cargo / Rol',
            'nombre_completo': 'Nombre y Apellido',
            'orden': 'Orden de jerarquía',
        }
        widgets = {
            'cargo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Presidente/a, Vicepresidente/a, Secretario/a'
            }),
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez'
            }),
            'orden': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1'
            }),
        }