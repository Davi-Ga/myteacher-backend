from django.db import models

class Professor (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    valor_hora = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.URLField(max_length=225, null=False, blank=False)

class Aula(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=False, blank=False, related_name='aulas')