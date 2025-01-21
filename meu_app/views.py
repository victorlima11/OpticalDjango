from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def contato(request):
    return render(request, 'contato.html')

def carrinho(request):
    return render(request, 'carrinho.html')

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
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'cadastro_usuario.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário em uso.")
            return render(request, 'cadastro_usuario.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já em uso.")
            return render(request, 'cadastro_usuario.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Usuário cadastrado com sucesso!")
                return redirect('home')
            else:
                messages.error(request, "Erro ao tentar fazer login após o cadastro.")
                return render(request, 'cadastro_usuario.html')

        except Exception as e:
            messages.error(request, f"Erro ao cadastrar usuário: {e}")
            return render(request, 'cadastro_usuario.html')

    return render(request, 'cadastro_usuario.html')

def produtos_lista(request):
    produtos = Produto.objects.all()
    return render (request, 'produtos.html', {'produtos': produtos})

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto_detalhes.html', {'produto': produto})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    usuario = request.user

    # Verifica se o usuário já possui um carrinho
    carrinho, criado = Carrinho.objects.get_or_create(usuario=usuario)

    # Verifica se o item já está no carrinho
    item, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('exibir_carrinho')

def exibir_carrinho(request):
    usuario = request.user
    carrinho = Carrinho.objects.filter(usuario=usuario).first()

    if not carrinho or not carrinho.itens.exists():
        return render(request, 'carrinho.html', {'mensagem': 'Seu carrinho está vazio.'})

    itens = carrinho.itens.all()
    total = sum(item.subtotal for item in itens)

    return render(request, 'carrinho.html', {'itens': itens, 'total': total})

def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return redirect('exibir_carrinho')
