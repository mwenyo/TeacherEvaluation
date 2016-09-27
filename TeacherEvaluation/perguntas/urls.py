from django.conf.urls import url
from perguntas import views

urlpatterns = [
        url(r'^(?P<id>\d+)/$', views.pergunta, name="pergunta"),
        url(r'^$', views.perguntas, name="perguntas"),
    ]