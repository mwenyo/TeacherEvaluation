from django.conf.urls import url
from coordenadores import views

urlpatterns = [
        #url(r'^(?P<id>\d+)/$', views.sala, name="sala"),
        url(r'^$', views.coordenadores, name="coordenadores"),
    ]