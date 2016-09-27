from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from perguntas.forms import PerguntaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from perguntas.models import Pergunta

# Create your views here.

@login_required(login_url='/')
def perguntas(request):from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from categorias.forms import CategoriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User
from categorias.models import Categoria
from perguntas.models import Pergunta

# Create your views here.

@login_required(login_url='/')
def categorias(request):
    lista = Categoria.objects.all()
    return render_to_response('categorias/categorias.html', {'lista': lista})

@login_required(login_url='/')
def categoria(request, id):
    objeto = get_object_or_404(Categoria, pk=id)
    if request.method == "GET":
        form = CategoriaForm(instance=objeto)
        perguntas_relacionadas = Pergunta.objects.filter(categoria_id=id)
        return render(request, 'categorias/categoria.html', {'objeto': objeto, 'perguntas_relacionadas': perguntas_relacionadas, 'form':form, 'user': User})
    else:
        form = CategoriaForm(request.POST, instance=objeto)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect('/categorias/')
        return render(request, 'categorias/categoria.html', {'objeto': objeto,'form':form})
    lista = Pergunta.objects.all()
    return render_to_response('categorias/categoria.html', {'lista': lista})