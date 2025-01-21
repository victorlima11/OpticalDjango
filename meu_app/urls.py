from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    # path('carrinho/', views.exibir_carrinho, name='exibir_carrinho'),
    # path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    # path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    # path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('produtos/', views.produtos_lista, name='produtos_lista'),
    path('produtos/<int:produto_id>/', views.produto_detalhes, name='produto_detalhes')
]




