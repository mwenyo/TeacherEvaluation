# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0002_pergunta_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='cabecalho',
            field=models.TextField(verbose_name='Cabeçalho'),
        ),
    ]
