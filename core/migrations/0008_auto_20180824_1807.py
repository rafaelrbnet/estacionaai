# Generated by Django 2.1 on 2018-08-24 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_mensalista'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pgto', models.DateField(verbose_name='Data da Cobrança')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Movimento Mensalista',
                'verbose_name_plural': 'Movimentos Mensalista',
            },
        ),
        migrations.AlterModelOptions(
            name='mensalista',
            options={'verbose_name': 'Mensalista', 'verbose_name_plural': 'Mensalista'},
        ),
        migrations.AddField(
            model_name='movmensalista',
            name='mensalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensalista', to='core.Mensalista', verbose_name='Mensalista'),
        ),
    ]