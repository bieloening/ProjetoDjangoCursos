from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='images/')
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome