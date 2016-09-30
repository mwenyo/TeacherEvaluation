from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from questionarios.forms import QuestionarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from questionarios.models import Questionario

# Create your views here.

@login_required(login_url='/')
def questionarios(request):
    lista = Questionario.objects.all()
    return render_to_response('questionarios/questionarios.html', {'lista': lista})

@login_required(login_url='/')
def questionario(request, id):
    objeto = get_object_or_404(Questionario, pk=id)
    if request.method == "GET":
        form = QuestionarioForm(instance=objeto)
        return render(request, 'questionarios/questionario.html', {'objeto': objeto, 'form':form, 'user': User})
    else:
        form = QuestionarioForm(request.POST, instance=objeto)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/questionarios/')
        return render(request, 'questionarios/questionario.html', {'objeto': objeto,'form':form})