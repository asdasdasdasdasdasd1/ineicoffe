# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, default=None, null=True)),
                ('tipo', models.PositiveIntegerField(choices=[(1, 'Interior'), (2, 'Exterior'), (3, 'Terraza')])),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('codigo', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(blank=True, default=None, help_text='referncia a la mesa', max_length=100, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('ambientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientes.Ambiente')),
            ],
        ),
    ]
