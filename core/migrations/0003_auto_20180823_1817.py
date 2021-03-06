# Generated by Django 2.1 on 2018-08-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor da hora')),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor do mês')),
                ('atual', models.BooleanField(blank=True, default=False, verbose_name='Ativo?')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Parâmeto',
                'verbose_name_plural': 'Parâmetos',
            },
        ),
        migrations.AlterModelOptions(
            name='corveiculo',
            options={'verbose_name': 'Cor', 'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='marcaveiculo',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AlterModelOptions(
            name='tamanhoveiculo',
            options={'verbose_name': 'Tamanho', 'verbose_name_plural': 'Tamanhos'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'Veículo', 'verbose_name_plural': 'Veículos'},
        ),
    ]
