from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from perguntas.forms import PerguntaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from perguntas.models import Pergunta

# Create your views here.

@login_required(login_url='/')
def perguntas(request):
    lista = Pergunta.objects.all()
    return render_to_response('perguntas/perguntas.html', {'lista': lista})

@login_required(login_url='/')
def pergunta(request, id):
    objeto = get_object_or_404(Pergunta, pk=id)
    if request.method == "GET":
        form = PerguntaForm(instance=objeto)
        return render(request, 'perguntas/pergunta.html', {'objeto': objeto, 'form':form, 'user': User})
    else:
        form = PerguntaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/perguntas/')
        return render(request, 'perguntas/pergunta.html', {'objeto': objeto,'form':form})