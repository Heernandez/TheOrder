# Generated by Django 3.0.2 on 2020-02-03 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedido', '0002_auto_20200202_2357'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='ListaItem',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='tipoEstado',
            new_name='tipoPedido',
        ),
    ]