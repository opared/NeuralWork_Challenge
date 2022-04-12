from django.urls import path, re_path

from . import views

app_name = 'filtros_app'

urlpatterns = [
    path(
        'cargar-viajes/',
        views.ViajesApiView.as_view(),
        name='cargar-viajes'
    ),
    path(
        'filtro-semana/',
        views.FiltroSemana.as_view(),
        name='filtro-semana'
    ),
    path(
        'filtro-coordenadas/',
        views.FiltroCoordenadas.as_view(),
        name='filtro-coordenadas'
    ),
    path(
        'filtro-hora/',
        views.FiltroHora.as_view(),
        name='filtro-hora'
    ),
    path(
        'filtro-fuente/',
        views.FiltroSource.as_view(),
        name='fuente-fuente'
    ),
    path(
        'filtro-region/',
        views.FiltroRegion.as_view(),
        name='fuente-region'
    ),
]
