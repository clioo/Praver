# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-11 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueble', '0017_auto_20180526_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='contadorVisitas',
            field=models.IntegerField(default=0),
        ),
    ]