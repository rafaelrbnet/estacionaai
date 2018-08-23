from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class MarcaVeiculo(models.Model):
    marca = models.CharField('Marca', max_length=50)

    def __str__(self):
        return self.marca

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class CorVeiculo(models.Model):
    cor = models.CharField('Cor predominante', max_length=50)

    def __str__(self):
        return self.cor

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'


class TamanhoVeiculo(models.Model):
    tamanho = models.CharField('Tamanho', max_length=50)

    def __str__(self):
        return self.tamanho

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'


class Veiculo(models.Model):
    proprietario = models.OneToOneField(
        Pessoa, verbose_name='Proprietário do veículo', related_name='ProprietarioVeiculo', on_delete=models.CASCADE
    )
    marca = models.OneToOneField(
        MarcaVeiculo, verbose_name='Marca do veículo', related_name='MarcaVeiculo', on_delete=models.CASCADE
    )
    cor = models.OneToOneField(
        CorVeiculo, verbose_name='Cor do veículo', related_name='CorVeiculo', on_delete=models.CASCADE
    )
    tamanho = models.OneToOneField(
        TamanhoVeiculo, verbose_name='Tamanho do veículo',  related_name='TamanhoVeiculo', on_delete=models.CASCADE
    )
    placa = models.CharField('Placa', max_length=7)
    avarias = models.TextField('Avarias existentes', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_at = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.marca, self.cor, self.placa)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
