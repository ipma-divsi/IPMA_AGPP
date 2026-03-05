from django.db import models

# Create your models here.
class User(models.Model):
    User = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


class User_passes(models.Model):
    encriptacao = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    expira_em = models.DateTimeField()

class Aplicacoes(models.Model):
    nome = models.CharField(max_length=100)
    versoes = models.CharField(max_length=100)
    fornecedores = models.CharField(max_length=100)

class Registo_de_aplicacoes (models.Model):
    data = models.DateTimeField(auto_now_add=True)

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    numero_inventario = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)

class Registo_equipamento(models.Model):
    data = models.DateTimeField(auto_now_add=True)

class Logs(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    observacoes = models.CharField(max_length=200)