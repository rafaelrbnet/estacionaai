from django.db import models
import math


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
    proprietario = models.ForeignKey(
        Pessoa, verbose_name='Proprietário do veículo', related_name='ProprietarioVeiculo', on_delete=models.CASCADE
    )
    marca = models.ForeignKey(
        MarcaVeiculo, verbose_name='Marca do veículo', related_name='MarcaVeiculo', on_delete=models.CASCADE
    )
    cor = models.ForeignKey(
        CorVeiculo, verbose_name='Cor do veículo', related_name='CorVeiculo', on_delete=models.CASCADE
    )
    tamanho = models.ForeignKey(
        TamanhoVeiculo, verbose_name='Tamanho do veículo',  related_name='TamanhoVeiculo', on_delete=models.CASCADE
    )
    placa = models.CharField('Placa', max_length=7)
    avarias = models.TextField('Avarias existentes', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.marca, self.cor, self.placa)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'


class Parametros(models.Model):
    valor_hora = models.DecimalField('Valor da hora', max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField('Valor do mês', max_digits=6, decimal_places=2)
    atual = models.BooleanField('Ativo?', blank=True, default=False)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def save(self, force_insert=False, force_update=False, **kwargs):
        instance = super(Parametros, self)
        instance.save(force_insert, force_update)
        if self.atual:
            pass
            # instance.exclude(pk=instance.pk).update(correct=False)
            # @todo Fazer o update de todos os parametros para false quando atualizar o registro

    def __str__(self):
        return 'Parâmetos Gerais valor hora: {} valor mês: {}'.format(self.valor_hora, self.valor_mes)

    class Meta:
        verbose_name = 'Parâmeto'
        verbose_name_plural = 'Parâmetos'


''' def post_save_parametros(instance, **kwargs):
    instance.thread.save()
    if instance.correct:
        instance.thread.replies.exclude(pk=instance.pk).update(correct=False)


models.signals.post_save.connect(
    post_save_parametros, sender=Parametros, dispatch_uid='post_save_parametros'
)'''


class MovRotativo(models.Model):
    entrada = models.DateTimeField('Data de entrada', auto_now=False)
    saida = models.DateTimeField('Data de saída', auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField('Valor da hora', max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(
        Veiculo, verbose_name='Veículo', related_name='veiculo', on_delete=models.CASCADE
    )
    pago = models.BooleanField('Pago?', default=False)

    # @todo O sistema não contempla uma permanencia minima, portanto 1 segundo de diferença equivale a uma hora
    def horas_total(self):
        if self.saida:
            return math.ceil((self.saida - self.entrada).total_seconds() / 3600)
        else:
            return 0

    def total(self):
        if self.saida:
            return self.valor_hora * self.horas_total()
        else:
            return 0

    def __str__(self):
        return self.veiculo.placa

    class Meta:
        verbose_name = 'Movimento Rotativo'
        verbose_name_plural = 'Movimentos Rotativo'


class Mensalista(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, verbose_name='Veículo', related_name='veiculo_mensal', on_delete=models.CASCADE
    )
    inicio = models.DateField('Início da Cobrança')
    valor_mes = models.DecimalField('Valor do mês', max_digits=6, decimal_places=2)

    def __str__(self):
        return '{} - {}'.format(self.veiculo, self.inicio)

    class Meta:
        verbose_name = 'Mensalista'
        verbose_name_plural = 'Mensalista'


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(
        Mensalista, verbose_name='Mensalista', related_name='mensalista', on_delete=models.CASCADE
    )
    dt_pgto = models.DateField('Data da Cobrança')
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{} - {}'.format(self.mensalista, self.total)

    class Meta:
        verbose_name = 'Movimento Mensalista'
        verbose_name_plural = 'Movimentos Mensalista'
