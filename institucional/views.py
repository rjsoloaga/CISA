from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import InformacionInstitucional
from .forms import InformacionInstitucionalForm

# Vista para editar o crear los datos institucionales
@login_required
def editar_institucional(request):
    institucional = InformacionInstitucional.objects.first()

    if request.method == 'POST':
        form = InformacionInstitucionalForm(request.POST, instance=institucional)
        if form.is_valid():
            form.save()
            return redirect('detalle_institucional')
    else:
        form = InformacionInstitucionalForm(instance=institucional)

    return render(request, 'institucional/institucional_form.html', {'form': form, 'institucional': institucional})

# Vista para visualizar la información actual
def detalle_institucional(request):
    institucional = InformacionInstitucional.objects.first()
    return render(request, 'institucional/institucional_detalle.html', {'institucional': institucional})