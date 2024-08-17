# Generated by Django 5.0.2 on 2024-03-03 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('turistic_package', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creado', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_salida', models.DateTimeField(verbose_name='Fecha de Salida')),
                ('precio', models.PositiveIntegerField(verbose_name='Precio del Vuelo')),
                ('aerolinea', models.CharField(choices=[('Delta Airlines', 'Delta Airlines'), ('Air Europa', 'Air Europa'), ('Interjet', 'Interjet')], max_length=50, verbose_name='Aerolínea')),
                ('imagen_vuelo', models.ImageField(null=True, upload_to='vuelos/', verbose_name='Imagen')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turistic_package.pais', verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Vuelo',
                'verbose_name_plural': 'Vuelos',
            },
        ),
    ]
