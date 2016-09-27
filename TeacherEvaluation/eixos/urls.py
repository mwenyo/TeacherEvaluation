from django.conf.urls import url
from eixos import views

urlpatterns = [
        url(r'^(?P<id>\d+)/$', views.eixo, name="eixo"),
        url(r'^$', views.eixos, name="eixos"),
    ]