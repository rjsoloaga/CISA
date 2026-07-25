from django.urls import path
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.vista_home, name='home'),
    path('crear/', views.noticias_crear, name='noticias_crear'),
    path('noticias/<int:pk>/', views.vista_noticia_detalle, name='noticias_detalle'),
    path('noticias/<int:pk>/editar/', views.noticias_editar, name='noticias_editar'),
    path('noticias/<int:pk>/eliminar/', views.noticias_eliminar, name='noticias_eliminar'),
    path('contacto/', views.vista_contacto, name='contacto'),
    path('cisa/', views.vista_cisa, name='cisa'),
    path('documentos/', views.vista_documentos, name='documentos'),
]