# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-16 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueble', '0014_auto_20180425_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=23, max_digits=28, null=True),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=23, max_digits=28, null=True),
        ),
    ]