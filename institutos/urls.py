from django.urls import path
from . import views

app_name = 'institutos'

urlpatterns = [
    path('', views.listar_institutos, name='listar'),
    path('crear/', views.instituto_crear, name='instituto_crear'),
    path('detalle/<int:pk>/', views.instituto_detalle, name='instituto_detalle'),
    path('editar/<int:pk>/', views.instituto_editar, name='instituto_editar'),
    path('eliminar/<int:pk>/', views.instituto_eliminar, name='instituto_eliminar'),
]