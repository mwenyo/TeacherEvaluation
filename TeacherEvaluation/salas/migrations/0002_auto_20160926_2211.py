# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
