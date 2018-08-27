from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    novo_pessoa,
    novo_veiculo,
    novo_mensalista,
    novo_movmensalista,
    novo_movrotativo
)

app_name = 'core'

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('novo-pessoa/', novo_pessoa, name='core_novo_pessoa'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('novo-veiculo/', novo_veiculo, name='core_novo_veiculo'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('novo-mov-rot/', novo_movrotativo, name='core_novo_movrotativo'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('novo-mensalistas/', novo_mensalista, name='core_novo_mensalista'),
    path('mov-men/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('novo-mov-men/', novo_movmensalista, name='core_novo_movmensalista'),
]
