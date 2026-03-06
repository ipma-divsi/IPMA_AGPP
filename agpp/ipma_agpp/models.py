
from django.db import models

class Grupos(models.Model):
   nome = models.CharField(max_length=100)
   data_inicio = models.DateField(auto_now_add=True)
   data_alteracao = models.DateField(auto_now_add=True)
   descricao = models.CharField(max_length=100)
   gerar_relatorio = models.BooleanField(default=True)
   ativo = models.BooleanField(default=True)

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    grupo = models.ForeignKey( Grupos,on_delete=models.CASCADE ,null=True, blank=True)


class User_passes(models.Model):
    encriptacao = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expira_em = models.DateTimeField()


class Aplicacoes(models.Model):
    nome = models.CharField(max_length=100)
    versoes = models.CharField(max_length=100)
    nomes = models.ManyToManyField(User, through='User_aplicacoes')
    fornecedores = models.CharField(max_length=100)


class User_aplicacoes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aplicacao = models.ForeignKey(Aplicacoes, on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(auto_now_add=True)
    atribuido_por = models.CharField(max_length=100)


class Registo_de_aplicacoes(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aplicacao = models.ForeignKey(Aplicacoes, on_delete=models.CASCADE)


class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    numero_inventario = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    aplicacao = models.ForeignKey(Aplicacoes, on_delete=models.CASCADE)


class Registo_equipamento(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    aplicacao = models.ForeignKey(Aplicacoes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Logs(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    observacoes = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logs_aplicacoes = models.ManyToManyField(Aplicacoes)
    logs_equipamentos = models.ManyToManyField(Equipamento)


