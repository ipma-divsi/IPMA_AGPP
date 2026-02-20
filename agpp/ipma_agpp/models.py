from django.db import models

# Create your models here.
class user(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
class user_passes:
    encriptacao = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    expira_em = models.DateTimeField()
    