from django.urls import path
from .views import (
    home, lista_pessoas, lista_veiculos, lista_movrotativos
)

app_name = 'core'

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot-list/', lista_movrotativos, name='core_lista_movrotativos'),
]
