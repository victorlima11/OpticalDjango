from django.db import models

class Usuario(models.Model):
    class Tipo(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        USER = 'user', 'Usuário'

    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True)
    senha = models.TextField(max_length=25, null=False, blank=False)
    telefone = models.TextField(max_length=15, null=False, blank=False)
    tipo = models.CharField(max_length= 50, choices=Tipo.choices, default=Tipo.USER)

    def __str__(self):
        return f"Nome: {self.nome} - Email: {self.email}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    imagem_url = models.URLField(max_length=500, null=True, blank=True)
    preco = models.FloatField(null=False, blank=False)
    marca = models.TextField(null=False, blank=False)
    tipo = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome
