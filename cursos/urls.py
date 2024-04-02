from django.urls import path
from . import views

urlpatterns = [
    path('listar_cursos/', views.listar_cursos, name="listar_cursos"),
    path('criar_curso/', views.criar_curso, name="criar_curso"),

]