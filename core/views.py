from django.shortcuts import render
from .models import Pessoa


def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {'pessoas': pessoas}
    return render(request, 'lista_pessoas.html', context)
