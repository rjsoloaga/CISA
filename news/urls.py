from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.vista_home, name='home'),
    path('crear/', views.noticias_crear, name='noticias_crear'),
    path('noticias/', views.listar_noticias, name='noticias_listar'),
    path('noticias/<int:pk>/', views.vista_noticia_detalle, name='noticias_detalle'),
    path('noticias/<int:pk>/editar/', views.noticias_editar, name='noticias_editar'),
    path('noticias/<int:pk>/eliminar/', views.noticias_eliminar, name='noticias_eliminar'),
    
    # Contacto y Redes Sociales
    path('contacto/', views.vista_contacto, name='contacto'),
    path('contacto/editar/', views.contacto_editar_info, name='contacto_editar_info'),
    path('contacto/eliminar-info/', views.contacto_eliminar_info, name='contacto_eliminar_info'),
    path('contacto/redes/nueva/', views.red_social_crear, name='red_social_crear'),
    path('contacto/redes/<int:pk>/editar/', views.red_social_editar, name='red_social_editar'),
    path('contacto/redes/<int:pk>/eliminar/', views.red_social_eliminar, name='red_social_eliminar'),
    path('contacto/limpiar/<str:campo>/', views.contacto_limpiar_campo, name='contacto_limpiar_campo'),
    path('contacto/adicional/nuevo/', views.contacto_adicional_crear, name='contacto_adicional_crear'),
    path('contacto/adicional/<int:pk>/editar/', views.contacto_adicional_editar, name='contacto_adicional_editar'),
    path('contacto/adicional/<int:pk>/eliminar/', views.contacto_adicional_eliminar, name='contacto_adicional_eliminar'),

    path('cisa/', views.vista_cisa, name='cisa'),
    path('documentos/', views.vista_documentos, name='documentos'),
]