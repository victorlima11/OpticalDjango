from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    imagem_url = models.URLField(max_length=500, null=True, blank=True)
    preco = models.FloatField(null=False, blank=False)  # Usando FloatField conforme sua estrutura
    marca = models.TextField(null=False, blank=False)
    genero = models.CharField(max_length=30, null=False, blank=False, default="Unissex")
    tipo = models.TextField(null=False, blank=False)
    

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemCarrinho)
    total = models.FloatField(null=False)  # Usando FloatField para o total, de acordo com o preço do produto
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido de {self.usuario.username} em {self.data_pedido}'
