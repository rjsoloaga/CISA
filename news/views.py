from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required

from .forms import (
    NoticiaForm,
    ContactoForm,
    InformacionContactoForm,
    RedSocialForm,
    DatoContactoAdicionalForm,
)
from .models import news, InformacionContacto, RedSocial, DatoContactoAdicional


# ==========================================
# GESTIÓN DE NOTICIAS
# ==========================================

@staff_member_required
def noticias_crear(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news:home')
    else:
        form = NoticiaForm()
    
    return render(request, 'news/crear_noticias.html', {'form': form})


@staff_member_required
def noticias_editar(request, pk):
    noticia = get_object_or_404(news, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('news:noticias_detalle', pk=pk)
    else:
        form = NoticiaForm(instance=noticia)
    
    return render(request, 'news/editar_noticia.html', {'form': form, 'noticia': noticia})


@staff_member_required
def noticias_eliminar(request, pk):
    noticia = get_object_or_404(news, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('news:home')
    return render(request, 'news/eliminar_noticia.html', {'noticia': noticia})


def vista_home(request):
    lista_noticias = news.objects.all().order_by('-fecha')[:3]
    return render(request, 'news/home.html', {'noticias': lista_noticias})


def listar_noticias(request):
    lista_noticias = news.objects.all().order_by('-fecha')
    return render(request, 'news/news.html', {'noticias': lista_noticias})


def vista_noticia_detalle(request, pk):
    noticia = get_object_or_404(news, pk=pk)
    return render(request, 'news/detalle_noticia.html', {'noticia': noticia})


# ==========================================
# CONTACTO Y REDES SOCIALES
# ==========================================

def vista_contacto(request):
    contacto = InformacionContacto.get_solo()
    redes = RedSocial.objects.all()
    datos_adicionales = DatoContactoAdicional.objects.all()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombreCompleto = form.cleaned_data.get('nombreCompleto')
            email_remitente = form.cleaned_data.get('email')
            asunto = form.cleaned_data.get('asunto')
            mensaje = form.cleaned_data.get('mensaje')

            cuerpo_mensaje = f"Mensaje recibido de: {nombreCompleto} ({email_remitente})\n\n{mensaje}"

            send_mail(
                subject=f"[Contacto CISA] {asunto}",
                message=cuerpo_mensaje,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "¡Tu mensaje fue enviado con éxito!")
            return redirect('news:contacto')
    else:
        form = ContactoForm()

    return render(request, 'news/contacto.html', {
        'form': form,
        'contacto': contacto,
        'redes': redes,
        'adicionales': datos_adicionales,
    })

    #-- CRUD Datos Adicionales de Contacto ---

@staff_member_required
def contacto_adicional_crear(request):
    if request.method == 'POST':
        form = DatoContactoAdicionalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nuevo campo de contacto agregado correctamente.")
            return redirect('news:contacto')
    else:
        form = DatoContactoAdicionalForm()
    return render(request, 'news/contacto_adicional_form.html', {'form': form, 'accion': 'Agregar'})

@staff_member_required
def contacto_adicional_editar(request, pk):
    dato = get_object_or_404(DatoContactoAdicional, pk=pk)
    if request.method == 'POST':
        form = DatoContactoAdicionalForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            messages.success(request, "Campo de contacto actualizado.")
            return redirect('news:contacto')
    else:
        form = DatoContactoAdicionalForm(instance=dato)
    return render(request, 'news/contacto_adicional_form.html', {'form': form, 'accion': 'Modificar'})

@staff_member_required
def contacto_adicional_eliminar(request, pk):
    dato = get_object_or_404(DatoContactoAdicional, pk=pk)
    if request.method == 'POST':
        dato.delete()
        messages.success(request, "Campo de contacto eliminado.")
        return redirect('news:contacto')
    return render(request, 'news/contacto_adicional_confirm_delete.html', {'dato': dato})


@staff_member_required
def contacto_editar_info(request):
    contacto = InformacionContacto.get_solo()
    if request.method == 'POST':
        form = InformacionContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos de contacto actualizados correctamente.")
            return redirect('news:contacto')
    else:
        form = InformacionContactoForm(instance=contacto)

    return render(request, 'news/contacto_editar.html', {'form': form})


@staff_member_required
def red_social_crear(request):
    if request.method == 'POST':
        form = RedSocialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Red social agregada exitosamente.")
            return redirect('news:contacto')
    else:
        form = RedSocialForm()

    return render(request, 'news/red_social_form.html', {
        'form': form,
        'accion': 'Agregar'
    })


@staff_member_required
def red_social_editar(request, pk):
    red = get_object_or_404(RedSocial, pk=pk)
    if request.method == 'POST':
        form = RedSocialForm(request.POST, instance=red)
        if form.is_valid():
            form.save()
            messages.success(request, "Red social modificada exitosamente.")
            return redirect('news:contacto')
    else:
        form = RedSocialForm(instance=red)

    return render(request, 'news/red_social_form.html', {
        'form': form,
        'accion': 'Modificar'
    })


@staff_member_required
def red_social_eliminar(request, pk):
    red = get_object_or_404(RedSocial, pk=pk)
    if request.method == 'POST':
        red.delete()
        messages.success(request, "Red social eliminada exitosamente.")
        return redirect('news:contacto')

    return render(request, 'news/red_social_confirm_delete.html', {
        'red': red
    })


# ==========================================
# OTRAS VISTAS INSTITUCIONALES DE NEWS
# ==========================================

def vista_cisa(request):
    return render(request, 'news/cisa.html')


def vista_documentos(request):
    return render(request, 'news/documentos.html')


@staff_member_required
def contacto_eliminar_info(request):
    contacto = InformacionContacto.get_solo()
    if request.method == 'POST':
        contacto.correo = "contacto@cisa.org.ar"
        contacto.telefono = ""
        contacto.direccion = ""
        contacto.horario_atencion = ""
        contacto.save()
        messages.success(request, "Datos de contacto restablecidos a los valores iniciales.")
        return redirect('news:contacto')

    return render(request, 'news/contacto_confirm_delete.html', {'contacto': contacto})

@staff_member_required
def contacto_limpiar_campo(request, campo):
    contacto = InformacionContacto.get_solo()
    if hasattr(contacto, campo):
        setattr(contacto, campo, "")
        contacto.save()
        messages.success(request, f"Se eliminó el dato de {campo.replace('_', ' ')} correctamente.")
    return redirect('news:contacto')