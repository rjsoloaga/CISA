from django import forms
from .models import InformacionInstitucional

class InformacionInstitucionalForm(forms.ModelForm):
    class Meta:
        model = InformacionInstitucional
        fields = ['nombre_presidente', 'correo', 'telefono', 'direccion']
        widgets = {
            'nombre_presidente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan Pérez'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contacto@asociacion.org'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+54 362 4000000'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle Falsa 123'}),
        }