from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalle_institucional, name='detalle_institucional'),
    path('agregar/', views.crear_autoridad, name='crear_autoridad'),
    path('editar/<int:pk>/', views.editar_autoridad, name='editar_autoridad'),
    path('eliminar/<int:pk>/', views.eliminar_autoridad, name='eliminar_autoridad'),
]