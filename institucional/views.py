from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Autoridad
from .forms import AutoridadForm

def es_staff(user):
    return user.is_authenticated and user.is_staff

def detalle_institucional(request):
    autoridades = Autoridad.objects.all()
    return render(request, 'institucional/institucional_detalle.html', {
        'autoridades': autoridades
    })

@user_passes_test(es_staff)
def crear_autoridad(request):
    if request.method == 'POST':
        form = AutoridadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autoridad agregada con éxito.")
            return redirect('detalle_institucional')
    else:
        form = AutoridadForm()

    return render(request, 'institucional/institucional_form.html', {
        'form': form,
        'accion': 'Agregar'
    })

@user_passes_test(es_staff)
def editar_autoridad(request, pk):
    autoridad = get_object_or_404(Autoridad, pk=pk)
    if request.method == 'POST':
        form = AutoridadForm(request.POST, instance=autoridad)
        if form.is_valid():
            form.save()
            messages.success(request, "Autoridad actualizada con éxito.")
            return redirect('detalle_institucional')
    else:
        form = AutoridadForm(instance=autoridad)

    return render(request, 'institucional/institucional_form.html', {
        'form': form,
        'accion': 'Modificar'
    })

@user_passes_test(es_staff)
def eliminar_autoridad(request, pk):
    autoridad = get_object_or_404(Autoridad, pk=pk)
    if request.method == 'POST':
        autoridad.delete()
        messages.success(request, f"{autoridad.cargo} eliminado correctamente.")
        return redirect('detalle_institucional')

    # Nombre exacto del archivo en institucional/templates/institucional/
    return render(request, 'institucional/institucional_confirm_delete.html', {
        'autoridad': autoridad
    })