from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def contato(request):
    return render(request, '#' )

def sobre(request):
    return render(request, '#')

def carrinho(request):
    return render (request, 'carrinho.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        imagem_url = request.POST.get('imagem_url')
        preco = request.POST.get('preco')
        marca = request.POST.get('marca')
        tipo = request.POST.get('tipo')

def cadastro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return HttpResponse("Erro, as senhas não coincidem")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Erro, nome de usuário em uso")
        if User.objects.filter(email=email).exists():
            return HttpResponse("Erro, email já em uso")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            # Realizar login automático após cadastro
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Usuário cadastrado com sucesso!")
                return redirect('home')  # Redirecionar para a página inicial após o cadastro
            else:
                return HttpResponse("Erro ao tentar fazer login após o cadastro.")
        except Exception as e:
            return HttpResponse(f"Erro ao cadastrar usuário: {e}. <a href='/cadastrar_usuario/'>Tente novamente</a>")

    return render(request, 'cadastro_usuario.html')

