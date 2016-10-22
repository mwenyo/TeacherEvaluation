# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0004_auto_20161022_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario_pergunta',
            name='resposta',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='questionario_pergunta',
            name='status',
            field=models.SmallIntegerField(default=-1),
        ),
    ]