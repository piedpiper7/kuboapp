# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0010_auto_20180226_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='instr',
            field=models.TextField(help_text='介绍', max_length=300, verbose_name='介绍'),
        ),
    ]