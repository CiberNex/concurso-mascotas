from django.urls import path
from . import views

urlpatterns = [
    path(
        'registrar/',
        views.registrar_mascota,
        name='registrar_mascota'
    ),
    path(
        'votar/<int:participacion_id>/',
        views.votar,
        name='votar'
    ),
    path(
        'galeria/<int:categoria_id>/',
        views.galeria,
        name='galeria'
    ),
]