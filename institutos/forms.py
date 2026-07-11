from django import forms
from .models import Instituto

class InstitutoForm(forms.ModelForm):

    class Meta:
        model = Instituto
        fields = ['nombre', 'logo', 'responsable', 'direccion', 'telefono', 'email', 'website', 'fundador', 'carisma', 'rama']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: Juan Perez'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-custom'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: Juan Perez'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'rows': 5, 'placeholder': 'Ej: Avenida 9 de julio'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: 362 - 4XXXXXX'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: ejemplo@email.com'}),
            'website': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: www.ejemplo.com.ar'}),
            'fundador': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: Breve reseña del fundador...'}),
            'carisma': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: Breve reseña del instituto...'}),
            'rama': forms.Select(attrs={'class': 'form-control form-control-custom'}),
        }