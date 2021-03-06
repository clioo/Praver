# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-04-14 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueble', '0008_auto_20180414_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='antiguedad',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='codigoPostal',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='latitud',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='longitud',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='numInt',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='precioRenta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='precioTraspaso',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='precioVenta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
