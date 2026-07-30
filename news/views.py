from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from news.forms import NoticiaForm
from .models import news


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


def vista_contacto(request):
    success = False
    if request.method == 'POST':
        # Simulated contact processing
        success = True
    return render(request, 'news/contacto.html', {'success': success})


def vista_cisa(request):
    return render(request, 'news/cisa.html')


def vista_documentos(request):
    return render(request, 'news/documentos.html')


