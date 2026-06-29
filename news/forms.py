from django import forms
from .models import news

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = news
        fields = ['titulo', 'resumen', 'cuerpo', 'imagen', 'ubicacion', 'fecha_evento', 'hora_evento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: Taller de Panadería'}),
            'resumen': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Breve resumen de la noticia'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control form-control-custom', 'rows': 5, 'placeholder': 'Escribe el contenido completo aquí...'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control form-control-custom'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Ej: Sede Central, Salón A'}),
            'fecha_evento': forms.DateInput(attrs={'class': 'form-control form-control-custom', 'type': 'date'}),
            'hora_evento': forms.TimeInput(attrs={'class': 'form-control form-control-custom', 'type': 'time'}),
        }