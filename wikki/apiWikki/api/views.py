from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .pagination import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class ProdutoList(APIView):
 def post(self, request):
  try:
       serializer = ProdutoSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Exception:
      return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 def get(self, request):
     try:
         lista_produto = Produto.objects.all()
         paginator = PaginacaoProduto()
         result_page = paginator.paginate_queryset(lista_produto, request)
         serializer = ProdutoSerializer(result_page, many=True)
         return paginator .get_paginated_response(serializer.data)
     except Exception:
         return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProdutoDetalhes(APIView):
   def get(self, request, pk):
       try:
           if pk == "0":
               return JsonResponse({'mensagem':
                "O ID deve ser maior que zero."}, status=status.HTTP_400_BAD_REQUEST)
           produto = Produto.objects.get(pk=pk)
           serializer = ProdutoSerializer(produto)
           return Response(serializer.data)
       except Produto.DoesNotExist:
           return JsonResponse({'mensagem': "O produto não existe"}, status=status.HTTP_404_NOT_FOUND)
       except Exception:
           return JsonResponse({'mensagem':
             "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   def put(self, request, pk):
       try:
           if pk == "0":
               return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                   status=status.HTTP_400_BAD_REQUEST)
           produto = Produto.objects.get(pk=pk)
           serializer = ProdutoSerializer(produto, data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Produto.DoesNotExist:
           return JsonResponse({'mensagem': "O produto não existe"},
                               status=status.HTTP_404_NOT_FOUND)
       except Exception:
           return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                               status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   def delete(self, request, pk):
       try:
           if pk == "0":
               return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                   status=status.HTTP_400_BAD_REQUEST)
           pedido_produto = Pedido.objects.filter(produdo_id=pk)
           if pedido_produto:
               return JsonResponse({'mensagem' :"O produto não pode ser excluido pois há pedidos relacionados a ele"},
                                   status=status.HTTP_403_FORBIDDEN)
           produto = Produto.objects.get(pk=pk)
           produto.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
       except Produto.DoesNotExist:
           return JsonResponse({'mensagem': "O produto não existe"},
                               status=status.HTTP_404_NOT_FOUND)
       except Exception:
           return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                               status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PedidoList(APIView):
 def post(self, request):
  try:
       serializer = PedidoSerializer(data=request.data)
       produto_id = request.data['produto']
       Produto.objects.get(pk=produto_id)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Produto.DoesNotExist:
      return JsonResponse({'mensagem': "O produto não existe"})
  except Exception:
      return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 def get(self, request):
      try:
          lista_pedido = Pedido.objects.all()
          paginator = PaginacaoPedido()
          result_page = paginator.paginate_queryset(lista_pedido, request)
          serializer = PedidoSerializer(result_page, many=True)
          return paginator.get_paginated_response(serializer.data)
      except Exception:
          return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PedidoDetalhes(APIView):
   def get(self, request, pk):
       try:
           if pk == "0":
               return JsonResponse({'mensagem':
                "O ID deve ser maior que zero."}, status=status.HTTP_400_BAD_REQUEST)
           pedido = Pedido.objects.get(pk=pk)
           serializer = PedidoSerializer(pedido)
           return Response(serializer.data)
       except Produto.DoesNotExist:
           return JsonResponse({'mensagem': "O pedido não existe"}, status=status.HTTP_404_NOT_FOUND)
       except Exception:
           return JsonResponse({'mensagem':
             "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   def put(self, request, pk):
       try:
           if pk == "0":
               return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                   status=status.HTTP_400_BAD_REQUEST)
           pedido = Pedido.objects.get(pk=pk)
           serializer = PedidoSerializer(pedido, data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Pedido.DoesNotExist:
           return JsonResponse({'mensagem': "O pedido não existe"},
                               status=status.HTTP_404_NOT_FOUND)
       except Exception:
           return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                               status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   def delete(self, request, pk):
       try:
           if pk == "0":
               return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                   status=status.HTTP_400_BAD_REQUEST)
           pedido = Pedido.objects.get(pk=pk)
           pedido.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
       except Pedido.DoesNotExist:
           return JsonResponse({'mensagem': "O pedido não existe"},
                               status=status.HTTP_404_NOT_FOUND)
       except Exception:
           return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                               status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UsuarioList(APIView):

 def post(self, request):
  try:
       serializer = UsuarioSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Exception:
      return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 def get(self, request):
      try:
          lista_usuario = Usuario.objects.all()
          paginator = PaginacaoUsuario()
          result_page = paginator.paginate_queryset(lista_usuario, request)
          serializer = UsuarioSerializer(result_page, many=True)
          return paginator.get_paginated_response(serializer.data)
      except Exception:
          return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)