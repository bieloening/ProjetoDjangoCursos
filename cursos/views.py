from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acessar_curso(request):
    return render(request, 'acessar_curso.html')

def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        return HttpResponse('Teste')
    