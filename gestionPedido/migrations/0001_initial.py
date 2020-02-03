# Generated by Django 3.0.2 on 2020-02-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPedido', models.IntegerField()),
                ('idProducto', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('detalle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.IntegerField(primary_key=True, serialize=False)),
                ('idEstado', models.IntegerField()),
                ('tipoEstado', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]
