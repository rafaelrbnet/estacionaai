from django.urls import path
from core import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.HomeView.as_view(), name='core_home'),
    path('pessoas/', core_views.ListaPessoasView.as_view(), name='core_lista_pessoas'),
    path('novo-pessoa/', core_views.novo_pessoa, name='core_novo_pessoa'),
    path('altera-pessoa/<pk>', core_views.altera_pessoa, name='core_altera_pessoa'),
    path('apaga-pessoa/<pk>', core_views.apaga_pessoa, name='core_apaga_pessoa'),

    path('veiculos/', core_views.ListaVeiculosView.as_view(), name='core_lista_veiculos'),
    path('novo-veiculo/', core_views.novo_veiculo, name='core_novo_veiculo'),
    path('altera-veiculo/<pk>', core_views.altera_veiculo, name='core_altera_veiculo'),
    path('apaga-veiculo/<pk>', core_views.apaga_veiculo, name='core_apaga_veiculo'),

    path('mov-rot/', core_views.lista_movrotativos, name='core_lista_movrotativos'),
    path('novo-mov-rot/', core_views.novo_movrotativo, name='core_novo_movrotativo'),
    path('altera-mov-rot/<pk>', core_views.altera_movrotativo, name='core_altera_movrotativo'),
    path('apaga-mov-rot/<pk>', core_views.apaga_movrotativo, name='core_apaga_movrotativo'),

    path('mensalistas/', core_views.lista_mensalistas, name='core_lista_mensalistas'),
    path('novo-mensalistas/', core_views.novo_mensalista, name='core_novo_mensalista'),
    path('altera-mensalistas/<pk>', core_views.altera_mensalista, name='core_altera_mensalista'),
    path('apaga-mensalistas/<pk>', core_views.apaga_mensalista, name='core_apaga_mensalista'),

    path('mov-men/', core_views.lista_movmensalistas, name='core_lista_movmensalistas'),
    path('novo-mov-men/', core_views.novo_movmensalista, name='core_novo_movmensalista'),
    path('altera-mov-men/<pk>', core_views.altera_movmensalista, name='core_altera_movmensalista'),
    path('apaga-mov-men/<pk>', core_views.apaga_movmensalista, name='core_apaga_movmensalista'),
]
