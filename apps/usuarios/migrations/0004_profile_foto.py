# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-06-14 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20180526_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
