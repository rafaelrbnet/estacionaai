from django.contrib import admin
from .models import (
    TamanhoVeiculo,
    MarcaVeiculo,
    Veiculo,
    CorVeiculo,
    Pessoa,
    Parametros,
    MovRotativo,
    Mensalista,
    MovMensalista,
)


class VeiculoAdmin(admin.ModelAdmin):

    list_display = ['proprietario', 'marca', 'cor', 'placa']
    search_fields = ['proprietario__nome', 'marca__marca', 'placa']
    list_filter = ['criado_em', 'tamanho__tamanho', 'marca__marca', 'cor__cor']


class ParametrosAdmin(admin.ModelAdmin):

    list_display = ['valor_hora', 'valor_mes', 'atual', 'criado_em', 'atualizado_em']
    list_filter = ['criado_em']


class MovRotativoAdmin(admin.ModelAdmin):

    # @todo aprender como renomeia os itens da grade
    list_display = ['veiculo', 'entrada', 'saida', 'valor_hora', 'pago', 'total', 'horas_total']
    # @todo aprender como coloca relacionamento na busca
    # search_fields = ['veiculo__marca']
    list_filter = ['entrada', 'saida', 'pago']


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ['mensalista', 'dt_pgto', 'total']
    list_filter = ['dt_pgto']


admin.site.register(TamanhoVeiculo)
admin.site.register(MarcaVeiculo)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(CorVeiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros, ParametrosAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista,MovMensalistaAdmin)



