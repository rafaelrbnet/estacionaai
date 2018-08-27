from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)
from .forms import PessoaForm, VeiculoForm, MovMensalistaForm, MensalistaForm, MovRotativoForm


def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {'pessoas': pessoas, 'form': PessoaForm}
    return render(request, 'lista_pessoas.html', context)


def novo_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_pessoas')


def altera_pessoa(request, pk):
    context = {}
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    context['pessoa'] = pessoa
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_pessoas')
    else:
        return render(request, 'update_pessoa.html', context)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos, 'form': VeiculoForm}
    return render(request, 'lista_veiculos.html', context)


def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_veiculos')


def altera_veiculo(request, pk):
    context = {}
    veiculo = Veiculo.objects.get(pk=pk)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    context['veiculo'] = veiculo
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_veiculos')
    else:
        return render(request, 'update_veiculo.html', context)


def lista_movrotativos(request):
    movrotativos = MovRotativo.objects.all()
    context = {'movrotativos': movrotativos, 'form': MovRotativoForm}
    return render(request, 'lista_movrotativos.html', context)


def novo_movrotativo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_movrotativos')


def altera_movrotativo(request, pk):
    context = {}
    movrotativo = MovRotativo.objects.get(pk=pk)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    context['movrotativo'] = movrotativo
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_movrotativos')
    else:
        return render(request, 'update_movrotativo.html', context)


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    context = {'mensalistas': mensalistas, 'form': MensalistaForm}
    return render(request, 'lista_mensalistas.html', context)


def novo_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_mensalistas')


def altera_mensalista(request, pk):
    context = {}
    mensalista = Mensalista.objects.get(pk=pk)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    context['mensalista'] = mensalista
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_mensalistas')
    else:
        return render(request, 'update_mensalista.html', context)


def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    context = {'movmensalistas': movmensalistas, 'form': MovMensalistaForm}
    return render(request, 'lista_movmensalistas.html', context)


def novo_movmensalista(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_movmensalistas')


def altera_movmensalista(request, pk):
    context = {}
    movmensalista = MovMensalista.objects.get(pk=pk)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    context['movmensalista'] = movmensalista
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_movmensalistas')
    else:
        return render(request, 'update_movmensalista.html', context)

