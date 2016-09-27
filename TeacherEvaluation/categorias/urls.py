from django.conf.urls import url
from categorias import views

urlpatterns = [
        url(r'^(?P<id>\d+)/$', views.categoria, name="categoria"),
        url(r'^$', views.categorias, name="categorias"),
    ]