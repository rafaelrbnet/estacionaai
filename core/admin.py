from django.contrib import admin
from .models import (
    TamanhoVeiculo,
    MarcaVeiculo,
    Veiculo,
    CorVeiculo,
    Pessoa,
    Parametros,
    MovRotativo,
)


class VeiculoAdmin(admin.ModelAdmin):

    list_display = ['proprietario', 'marca', 'cor', 'placa']
    search_fields = ['proprietario__nome', 'marca__marca', 'placa']
    list_filter = ['criado_em', 'tamanho__tamanho', 'marca__marca', 'cor__cor']


class ParametrosAdmin(admin.ModelAdmin):

    list_display = ['valor_hora', 'valor_mes', 'atual', 'criado_em', 'atualizado_em']
    list_filter = ['criado_em']


class MovRotativoAdmin(admin.ModelAdmin):

    # @todo colocar o relacionamento do veículo na grade
    list_display = ['get_veiculo','entrada', 'saida', 'valor_hora', 'pago', 'total', 'horas_total']
    search_fields = ['veiculo__veiculo']
    list_filter = ['entrada', 'saida', 'pago']


admin.site.register(TamanhoVeiculo)
admin.site.register(MarcaVeiculo)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(CorVeiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros, ParametrosAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)



