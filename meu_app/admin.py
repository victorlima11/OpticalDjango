from django.contrib import admin
from .models import Produto, Carrinho, ItemCarrinho, Pedido


admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Carrinho)
