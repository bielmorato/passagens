from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('minhaconsulta', views.revisao_consulta, name='minha_consulta')
]
