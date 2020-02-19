from rest_framework import serializers
from .models import *


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "preco",
                  "data_criacao", "estoque"]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nome", "senha", "email",
                  "primeiro_nome", "ultimo_nome", "endereco"]

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "preco", "data_criacao", "estoque",
                  "produto", "usuario"]