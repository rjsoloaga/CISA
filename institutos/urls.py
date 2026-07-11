from django.urls import path
from . import views
app_name = 'institutos'

urlpatterns = [
    path('', views.listar_institutos, name='listar'),
    path('crear/', views.instituto_crear, name='crear'),
    path('editar/<int:pk>/', views.instituto_editar, name='editar'),
    path('eliminar/<int:pk>/', views.instituto_eliminar, name='eliminar')
]