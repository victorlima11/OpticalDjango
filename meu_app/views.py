from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.views import View
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def contato(request):
    return render(request, 'contato.html')

@login_required
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
  
def minha_view(request):
    context = {
        "phone": "85999381801",
    }
    return render(request, 'whatsapp_button.html', context)

def produtos_lista(request):
    produtos = Produto.objects.all()
    return render (request, 'produtos.html', {'produtos': produtos})

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto_detalhes.html', {'produto': produto})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    usuario = request.user

    carrinho, criado = Carrinho.objects.get_or_create(usuario=usuario)

    item, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('exibir_carrinho')

@login_required
def exibir_carrinho(request):
    usuario = request.user
    carrinho = Carrinho.objects.filter(usuario=usuario).first()

    if not carrinho or not carrinho.itens.exists():
        return render(request, 'carrinho.html', {'mensagem': 'Seu carrinho está vazio.'})

    itens = carrinho.itens.all()
    total = sum(item.subtotal for item in itens)

    return render(request, 'carrinho.html', {'itens': itens, 'total': total})


@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)

    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()

    return redirect('exibir_carrinho')


@login_required
def remover_tudo_do_carrinho(request, item_id):
    usuario = request.user
    carrinho = Carrinho.objects.filter(usuario=usuario).first()

    if carrinho:
        item = carrinho.itens.filter(id=item_id).first()

        if item:
            item.delete()

    return redirect('exibir_carrinho')


@login_required
def adicionar(request, produto_id):
    item = get_object_or_404(ItemCarrinho, id=produto_id)

    item.quantidade += 1
    item.save()

    return redirect('exibir_carrinho')

def lista_produtos(request):
    tipo = request.GET.get('tipo', '')
    marca = request.GET.get('marca', '')
    genero = request.GET.get('genero', '')

    produtos = Produto.objects.all()
    if tipo:
        produtos = produtos.filter(tipo=tipo)
    if marca:
        produtos = produtos.filter(marca=marca)
    if genero:
        produtos = produtos.filter(genero=genero)

    return render(request, 'produtos.html', {'produtos': produtos})

@login_required
def checkout(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        endereco = request.POST.get("endereco")
        cidade = request.POST.get("cidade")
        metodo_pagamento = request.POST.get("metodo_pagamento")

        return HttpResponse(f"""
            <h1>Dados Recebidos</h1>
            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Endereço:</strong> {endereco}</p>
            <p><strong>Cidade:</strong> {cidade}</p>
            <p><strong>Método de Pagamento:</strong> {metodo_pagamento}</p>
            <a href="/checkout/">Voltar ao checkout</a>
        """)

    return render(request, "checkout.html")

@login_required
def finalizar_pedido(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        metodo_pagamento = request.POST.get('pagamento')

        try:
            carrinho = get_object_or_404(Carrinho, usuario=request.user)
        except Carrinho.DoesNotExist:
            return render(request, 'erro.html', {'mensagem': 'Carrinho não encontrado.'})

        itens_carrinho = carrinho.itens.all()

        if not itens_carrinho.exists():
            return render(request, 'erro.html', {'mensagem': 'Seu carrinho está vazio.'})

        total = sum(item.subtotal for item in itens_carrinho)

        pedido = Pedido.objects.create(
            usuario=request.user,
            total=total,
        )

        # Associa os itens do carrinho ao pedido
        for item in itens_carrinho:
            pedido.produtos.add(item)  # Correção para usar 'produtos'

        # Salvar o pedido
        pedido.save()

        # Limpar o carrinho após finalizar o pedido
        carrinho.itens.all().delete()

        # Redirecionar para a página de sucesso
        return render(request, 'sucesso.html', {
            'nome': nome,
            'metodo_pagamento': metodo_pagamento,
            'total': total,
            'pedido': pedido,
        })
    else:
        # Redirecionar para o checkout caso o método não seja POST
        return redirect('checkout')

