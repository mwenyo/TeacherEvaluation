from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from salas.forms import SalaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from salas.models import Sala
from turmas.models import Turma

# Create your views here.

@login_required(login_url='/')
def salas(request):
    lista = Sala.objects.all()
    return render_to_response('salas/salas.html', {'lista': lista})

@login_required(login_url='/')
def sala(request, id):
    objeto = get_object_or_404(Sala, pk=id)
    if request.method == "GET":
        form = SalaForm(instance=objeto)
        turmas_relacionadas = Turma.objects.filter(sala_id=id)
        return render(request, 'salas/sala.html', {'objeto': objeto, 'turmas_relacionadas': turmas_relacionadas, 'form':form, 'user': User})
    else:
        form = SalaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/salas/')
        return render(request, 'salas/sala.html', {'objeto': objeto,'form':form})