from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
)

app_name = 'core'

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mov-men/', lista_movmensalistas, name='core_lista_movmensalistas'),
]
