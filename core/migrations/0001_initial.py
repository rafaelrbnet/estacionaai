# Generated by Django 2.1 on 2018-08-23 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=50, verbose_name='Cor predominante')),
            ],
        ),
        migrations.CreateModel(
            name='MarcaVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='TamanhoVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=50, verbose_name='Tamanho')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7, verbose_name='Placa')),
                ('avarias', models.TextField(blank=True, verbose_name='Avarias existentes')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_at', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('cor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CorVeiculo', to='core.CorVeiculo', verbose_name='Cor do veículo')),
                ('marca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MarcaVeiculo', to='core.MarcaVeiculo', verbose_name='Marca do veículo')),
                ('tamanho', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='TamanhoVeiculo', to='core.TamanhoVeiculo', verbose_name='Tamanho do veículo')),
            ],
        ),
    ]