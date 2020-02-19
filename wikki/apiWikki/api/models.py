from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=30, null=False)
    descricao = models.TextField(null=False)
    preco = models.FloatField(null=False)
    data_criacao = models.DateField()
    estoque = models.IntegerField(null=False)


class Usuario(models.Model):
    nome = models.CharField(max_length=30, null=False)
    senha = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=30, null=False)
    primeiro_nome = models.CharField(max_length=20, null=False)
    ultimo_nome = models.CharField(max_length=20, null=False)
    endereco = models.CharField(max_length=40, null=False)


class Pedido(models.Model):
    produto = models.ForeignKey(to='produto', on_delete=models.CASCADE)
    usuario = models.ForeignKey(to='usuario', on_delete=models.CASCADE)
    preco = models.FloatField(null=False)
    data_criacao = models.DateField()
    estoque = models.IntegerField(null=False)


from django.db import models

# Create your models here.
