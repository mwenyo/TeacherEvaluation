from django.conf.urls import url
from questionarios import views

urlpatterns = [
        url(r'^(?P<id>\d+)/$', views.questionario, name="questionario"),
        url(r'^$', views.questionarios, name="questionarios"),
    ]