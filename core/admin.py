from django.contrib import admin
from .models import TamanhoVeiculo, MarcaVeiculo, Veiculo, CorVeiculo, Pessoa


class VeiculoAdmin(admin.ModelAdmin):

    list_display = ['proprietario', 'marca', 'cor', 'placa']
    search_fields = ['proprietario__nome', 'marca__marca' , 'placa']
    list_filter = ['criado_em', 'tamanho__tamanho', 'marca__marca', 'cor__cor']


admin.site.register(TamanhoVeiculo)
admin.site.register(MarcaVeiculo)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(CorVeiculo)
admin.site.register(Pessoa)



