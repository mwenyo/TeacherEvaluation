# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 01:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'professores'},
        ),
    ]
