# Generated by Django 2.1 on 2018-08-27 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180824_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CorVeiculo', to='core.CorVeiculo', verbose_name='Cor do veículo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MarcaVeiculo', to='core.MarcaVeiculo', verbose_name='Marca do veículo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='tamanho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TamanhoVeiculo', to='core.TamanhoVeiculo', verbose_name='Tamanho do veículo'),
        ),
    ]
