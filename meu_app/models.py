from django.db import models
    
class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    imagem_url = models.URLField(max_length=500, null=True, blank=True)
    preco = models.FloatField(null=False, blank=False)
    marca = models.TextField(null=False, blank=False)
    tipo = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome
