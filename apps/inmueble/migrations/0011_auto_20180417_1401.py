# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-04-17 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueble', '0010_auto_20180414_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesinmbueble',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
