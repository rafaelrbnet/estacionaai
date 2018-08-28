from django.urls import path
from .views import (
    home,
    lista_pessoas, lista_veiculos, lista_movrotativos, lista_mensalistas, lista_movmensalistas,
    novo_pessoa, novo_veiculo, novo_mensalista, novo_movmensalista, novo_movrotativo,
    altera_pessoa, altera_veiculo, altera_movrotativo, altera_mensalista, altera_movmensalista,
    apaga_pessoa, apaga_veiculo, apaga_mensalista, apaga_movmensalista, apaga_movrotativo
)

app_name = 'core'

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('novo-pessoa/', novo_pessoa, name='core_novo_pessoa'),
    path('altera-pessoa/<pk>', altera_pessoa, name='core_altera_pessoa'),
    path('apaga-pessoa/<pk>', apaga_pessoa, name='core_apaga_pessoa'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('novo-veiculo/', novo_veiculo, name='core_novo_veiculo'),
    path('altera-veiculo/<pk>', altera_veiculo, name='core_altera_veiculo'),
    path('apaga-veiculo/<pk>', apaga_veiculo, name='core_apaga_veiculo'),

    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('novo-mov-rot/', novo_movrotativo, name='core_novo_movrotativo'),
    path('altera-mov-rot/<pk>', altera_movrotativo, name='core_altera_movrotativo'),
    path('apaga-mov-rot/<pk>', apaga_movrotativo, name='core_apaga_movrotativo'),

    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('novo-mensalistas/', novo_mensalista, name='core_novo_mensalista'),
    path('altera-mensalistas/<pk>', altera_mensalista, name='core_altera_mensalista'),
    path('apaga-mensalistas/<pk>', apaga_mensalista, name='core_apaga_mensalista'),

    path('mov-men/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('novo-mov-men/', novo_movmensalista, name='core_novo_movmensalista'),
    path('altera-mov-men/<pk>', altera_movmensalista, name='core_altera_movmensalista'),
    path('apaga-mov-men/<pk>', apaga_movmensalista, name='core_apaga_movmensalista'),
]
