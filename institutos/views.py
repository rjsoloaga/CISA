from django.contrib.admin.views.decorators import staff_member_required
from institutos.forms import InstitutoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Instituto

def listar_institutos(request):
    institutos = Instituto.objects.all()
    return render(request, 'institutos/listar.html', {'institutos' : institutos})

"""EJEMPLO DE LA FUNCION ANTERIOR PERO CON class
class InstitutoListView(ListView):
    model = Instituto
    template_name = 'institutos/listar.html'
    context_object_name = 'institutos'
    """

@staff_member_required
def instituto_crear(request):
    if request.method == 'POST':
        form = InstitutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('institutos:listar')
    else:
        form = InstitutoForm()
    return render(request, 'institutos/instituto_form.html', {'form' : form})

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

    return render(request, 'institutos/instituto_form.html', {'form' : form, 'instituto' : instituto})


@staff_member_required
def instituto_eliminar(request, pk):
    instituto = get_object_or_404(Instituto, pk=pk)
    if request.method == 'POST':
        instituto.delete()
        return redirect('institutos:listar')
    else:
        return render(request, 'institutos/instituto_confirm_delete.html', {'instituto' : instituto})

    
