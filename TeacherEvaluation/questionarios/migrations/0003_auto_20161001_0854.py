# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0002_auto_20160930_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionario',
            old_name='pergunta',
            new_name='perguntas',
        ),
    ]