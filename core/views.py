from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)
from .forms import PessoaForm, VeiculoForm, MovMensalistaForm, MensalistaForm, MovRotativoForm
from django.contrib.auth.decorators import login_required


def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'index.html', context)


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {'pessoas': pessoas, 'form': PessoaForm}
    return render(request, 'lista_pessoas.html', context)


@login_required
def novo_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "Pessoa criada com sucesso")
        form.save()
    return redirect('core:core_lista_pessoas')


@login_required
def altera_pessoa(request, pk):
    context = {}
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    context['pessoa'] = pessoa
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoa alterada com sucesso")
            return redirect('core:core_lista_pessoas')
    else:
        return render(request, 'update_pessoa.html', context)


@login_required
def apaga_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, "Pessoa apagada com sucesso")
        return redirect('core:core_lista_pessoas')
    else:
        context = {'objeto': pessoa, 'url_objeto': 'core:core_apaga_pessoa'}
        return render(request, 'delete_confirm.html', context)


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos, 'form': VeiculoForm}
    return render(request, 'lista_veiculos.html', context)


@login_required
def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_veiculos')


@login_required
def altera_veiculo(request, pk):
    context = {}
    veiculo = get_object_or_404(Veiculo, pk=pk)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    context['veiculo'] = veiculo
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_veiculos')
    else:
        return render(request, 'update_veiculo.html', context)


@login_required
def apaga_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core:core_lista_veiculos')
    else:
        context = {'objeto': veiculo, 'url_objeto': 'core:core_apaga_veiculo'}
        return render(request, 'delete_confirm.html', context)


@login_required
def lista_movrotativos(request):
    movrotativos = MovRotativo.objects.all()
    context = {'movrotativos': movrotativos, 'form': MovRotativoForm}
    return render(request, 'lista_movrotativos.html', context)


@login_required
def novo_movrotativo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_movrotativos')


@login_required
def altera_movrotativo(request, pk):
    context = {}
    movrotativo = get_object_or_404(MovRotativo, pk=pk)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    context['movrotativo'] = movrotativo
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_movrotativos')
    else:
        return render(request, 'update_movrotativo.html', context)


@login_required
def apaga_movrotativo(request, pk):
    movrotativo = get_object_or_404(MovRotativo, pk=pk)
    if request.method == 'POST':
        movrotativo.delete()
        return redirect('core:core_lista_movrotativos')
    else:
        context = {'objeto': movrotativo, 'url_objeto': 'core:core_apaga_movrotativo'}
        return render(request, 'delete_confirm.html', context)


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    context = {'mensalistas': mensalistas, 'form': MensalistaForm}
    return render(request, 'lista_mensalistas.html', context)


@login_required
def novo_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_mensalistas')


@login_required
def altera_mensalista(request, pk):
    context = {}
    mensalista = get_object_or_404(Mensalista, pk=pk)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    context['mensalista'] = mensalista
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_mensalistas')
    else:
        return render(request, 'update_mensalista.html', context)


@login_required
def apaga_mensalista(request, pk):
    mensalista = get_object_or_404(Mensalista, pk=pk)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core:core_lista_mensalistas')
    else:
        context = {'objeto': mensalista, 'url_objeto': 'core:core_apaga_mensalista'}
        return render(request, 'delete_confirm.html', context)


@login_required
def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    context = {'movmensalistas': movmensalistas, 'form': MovMensalistaForm}
    return render(request, 'lista_movmensalistas.html', context)


@login_required
def novo_movmensalista(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core:core_lista_movmensalistas')


@login_required
def altera_movmensalista(request, pk):
    context = {}
    movmensalista = get_object_or_404(MovMensalista, pk=pk)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    context['movmensalista'] = movmensalista
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core:core_lista_movmensalistas')
    else:
        return render(request, 'update_movmensalista.html', context)


@login_required
def apaga_movmensalista(request, pk):
    movmensalista = get_object_or_404(MovMensalista, pk=pk)
    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core:core_lista_movmensalistas')
    else:
        context = {'objeto': movmensalista, 'url_objeto': 'core:core_apaga_movmensalista'}
        return render(request, 'delete_confirm.html', context)
