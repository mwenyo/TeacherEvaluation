from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from salas.forms import SalaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from coordenadores.models import Coordenador
from professores.models import Professor

@login_required(login_url='/')
def coordenadores(request):
    lista = Coordenador.objects.all()
    return render_to_response('coordenadores/coordenadores.html', {'lista': lista})
