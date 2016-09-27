# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 02:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salas', '0001_initial'),
        ('cursos', '0001_initial'),
        ('periodos_letivos', '0002_auto_20160620_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('ano', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('turno', models.CharField(max_length=200)),
                ('ativo', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.Curso')),
                ('periodo_letivo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periodos_letivos.PeriodoLetivo')),
                ('sala_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.Sala')),
            ],
        ),
    ]
