# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0002_auto_20160620_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='eixo_id',
            new_name='eixo',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]
