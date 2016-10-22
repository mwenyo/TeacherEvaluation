# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0003_auto_20161001_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario_pergunta',
            name='status',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='questionario_pergunta',
            name='resposta',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=3),
        ),
    ]
