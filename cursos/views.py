from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.
def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    
    if nome_filtrar:
        cursos = Curso.objects.filter(nome__contains=nome_filtrar)
    else:
        cursos = Curso.objects.all()
    
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')
        print(status)
        
        return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        nome_digitado= request.POST.get('nome')
        carga_horaria_digitado = request.POST.get('carga_horaria')
        
        curso = Curso(
            nome = nome_digitado,
            carga_horaria = carga_horaria_digitado,
            data_criacao=datetime.now()
            
        )
        
        curso.save()
        return redirect('/curso/criar_curso/?status=1' )
    