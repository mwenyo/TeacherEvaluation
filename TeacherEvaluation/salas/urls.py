from django.conf.urls import url
from salas import views

urlpatterns = [
        url(r'^(?P<id>\d+)/$', views.sala, name="sala"),
        url(r'^$', views.salas, name="salas"),
    ]