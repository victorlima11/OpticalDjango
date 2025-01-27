from django.contrib import admin
from .models import Produto, Carrinho, ItemCarrinho, Pedido

admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)
admin.site.register(Pedido)