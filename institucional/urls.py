from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalle_institucional, name='detalle_institucional'),
    
    path('editar/', views.editar_institucional, name='editar_institucional'),
]