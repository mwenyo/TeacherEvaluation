from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from eixos.forms import EixoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from eixos.models import Eixo
from cursos.models import Curso

# Create your views here.

@login_required(login_url='/')
def eixos(request):
    lista = Eixo.objects.all()
    return render_to_response('eixos/eixos.html', {'lista': lista})

@login_required(login_url='/')
def eixo(request, id):
    objeto = get_object_or_404(Eixo, pk=id)
    if request.method == "GET":
        form = EixoForm(instance=objeto)
        cursos_relacionados = Curso.objects.filter(eixo_id=id)
        return render(request, 'eixos/eixo.html', {'objeto': objeto, 'cursos_relacionados':cursos_relacionados, 'form':form, 'user': User})
    else:
        form = EixoForm(request.POST, instance=objeto)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/eixos/')
        return render(request, 'eixos/eixo.html', {'objeto': objeto,'form':form})