from django.db import models

class  Curso(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)

