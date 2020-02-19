from django.conf.urls import url

from .views import *

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [

    url(r'^produto$', ProdutoList.as_view()),
    url(r'^produto/(?P<pk>[0-9]+)$', ProdutoDetalhes.as_view()),

    url(r'^pedido$', PedidoList.as_view()),
    url(r'^pedido/(?P<pk>[0-9]+)$', PedidoDetalhes.as_view()),

    url(r'^usuario$', UsuarioList.as_view()),


]