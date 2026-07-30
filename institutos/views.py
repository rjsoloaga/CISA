from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Instituto
from .forms import InstitutoForm

def listar_institutos(request):
    institutos = Instituto.objects.all()
    return render(request, 'institutos/listar.html', {'institutos': institutos})

def instituto_detalle(request, pk):
    instituto = get_object_or_404(Instituto, pk=pk)
    return render(request, 'institutos/detalle.html', {'instituto': instituto})

@staff_member_required
def instituto_crear(request):
    if request.method == 'POST':
        form = InstitutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('institutos:listar')
    else:
        form = InstitutoForm()
    return render(request, 'institutos/instituto_form.html', {
        'form': form,
        'titulo_pagina': 'Nuevo Instituto'
    })

@staff_member_required
def instituto_editar(request, pk):
    instituto = get_object_or_404(Instituto, pk=pk)
    if request.method == 'POST':
        form = InstitutoForm(request.POST, request.FILES, instance=instituto)
        if form.is_valid():
            form.save()
            return redirect('institutos:listar')
    else:
        form = InstitutoForm(instance=instituto)

    return render(request, 'institutos/instituto_form.html', {
        'form': form,
        'instituto': instituto,
        'titulo_pagina': f'Editar: {instituto.nombre}'
    })

@staff_member_required
def instituto_eliminar(request, pk):
    instituto = get_object_or_404(Instituto, pk=pk)
    if request.method == 'POST':
        instituto.delete()
        return redirect('institutos:listar')
    return render(request, 'institutos/instituto_confirm_delete.html', {'instituto': instituto})


def instituto_detalle(request, pk):
    instituto = get_object_or_404(Instituto, pk=pk)
    return render(request, 'institutos/detalle.html', {'instituto': instituto})