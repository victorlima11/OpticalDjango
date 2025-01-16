from django.urls import path
from . import views

# app_name = 'meu_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contato/', views.contato, name='contato'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
]




