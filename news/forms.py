from django import forms
from .models import  news,InformacionContacto,RedSocial,DatoContactoAdicional


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


        

class InformacionContactoForm(forms.ModelForm):
    class Meta:
        model = InformacionContacto
        fields = ['correo', 'direccion', 'telefono', 'whatsapp', 'horario_atencion']
        labels = {
            'correo': 'Correo Electrónico',
            'direccion': 'Dirección Central',
            'telefono': 'Teléfono Fijo',
            'whatsapp': 'WhatsApp (Ej: +54 9 11 4567 8901)',
            'horario_atencion': 'Horario de Atención',
        }
        widgets = {
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contacto@cisa.org.ar'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Av. General Paz 7890...'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+54 (11) 4567-8901'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+54 (11) 4567-8901'}),
            'horario_atencion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lunes a Viernes de 9:00 a 18:00 hs.'}),
        }

class RedSocialForm(forms.ModelForm):
    class Meta:
        model = RedSocial
        fields = ['nombre', 'url', 'icono', 'orden']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Instagram'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'icono': forms.Select(attrs={'class': 'form-select'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}),
        }

        from .models import DatoContactoAdicional

class DatoContactoAdicionalForm(forms.ModelForm):
    class Meta:
        model = DatoContactoAdicional
        fields = ['etiqueta', 'valor', 'tipo', 'icono', 'orden']
        labels = {
            'etiqueta': 'Nombre del Registro (Ej: Sede Anexo, Correo Secundario)',
            'valor': 'Contenido o Valor',
            'tipo': 'Tipo de Dato',
            'icono': 'Ícono',
            'orden': 'Orden de Visualización',
        }
        widgets = {
            'etiqueta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Sede Anexo'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Sarmiento 123 o anexo@cisa.org.ar'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'icono': forms.Select(attrs={'class': 'form-select'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}),
        }