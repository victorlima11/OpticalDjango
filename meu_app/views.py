from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        # Aqui você pode tratar a autenticação do usuário
        username = request.POST['username']
        password = request.POST['password']
        # Autenticação do usuário pode ser realizada aqui
    return render(request, 'login.html')

# Create your views here.
