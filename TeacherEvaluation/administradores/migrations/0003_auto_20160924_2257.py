# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administradores', '0002_auto_20160621_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='cargo',
            field=models.CharField(default='Pedagogo', max_length=200),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='setor',
            field=models.CharField(default='Pedagogia', max_length=200),
        ),
    ]
