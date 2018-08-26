from django.shortcuts import render


def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'index.html', context)
