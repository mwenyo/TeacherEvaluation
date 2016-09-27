"""
Definition of urls for TeacherEvaluation.
"""

from django.conf.urls import include, url
from django.contrib import admin    
from TeacherEvaluation import views
from salas import urls as salas
from eixos import urls as eixos
from perguntas import urls as perguntas
from categorias import urls as categorias
from coordenadores import urls as coordenadores
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^salas/', include(salas)),
    url(r'^categorias/', include(categorias)),
    url(r'^perguntas/', include(perguntas)),
    url(r'^eixos/', include(eixos)),
    url(r'^coordenadores/', include(coordenadores)),
    url(r'^admin/', include(admin.site.urls)),
]
