from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.
def home(request):
    # Obtém os cursos em destaque
    cursos_destaque = Curso.objects.all()[:3]  # Suponha que você deseja exibir apenas os primeiros 3 cursos em destaque

    # Renderiza o template 'home.html' e passa os cursos em destaque como contexto
    return render(request, 'home.html', {'cursos_destaque': cursos_destaque})

def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    carga_horaria_filtrar = request.GET.get('carga_horaria')
    
    cursos = Curso.objects.all()
    
    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)
        
    if carga_horaria_filtrar:
        cursos = cursos.filter(carga_horaria__gte=carga_horaria_filtrar)
    
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')
        print(status)
        
        return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        nome_digitado= request.POST.get('nome')
        carga_horaria_digitado = request.POST.get('carga_horaria')
        descricao_digitado = request.POST.get('descricao')
        
        curso = Curso(
            nome = nome_digitado,
            carga_horaria = carga_horaria_digitado,
            descricao = descricao_digitado,
            data_criacao=datetime.now()
        )
        curso.save()
        return redirect('/criar_curso/?status=1' )
    
def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    print(curso)
    return render(request, 'ver_curso.html', {'curso': curso})

def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.ativo = False
    curso.save()
    return redirect('/listar_cursos')