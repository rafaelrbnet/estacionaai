from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)


def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {'pessoas': pessoas}
    return render(request, 'lista_pessoas.html', context)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos}
    return render(request, 'lista_veiculos.html', context)


def lista_movrotativos(request):
    movrotativos = MovRotativo.objects.all()
    context = {'movrotativos': movrotativos}
    return render(request, 'lista_movrotativos.html', context)


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    context = {'mensalistas': mensalistas}
    return render(request, 'lista_mensalistas.html', context)


def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    context = {'movmensalistas': movmensalistas}
    return render(request, 'lista_movmensalistas.html', context)