# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180205_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='images/default.jpg', help_text='图片', upload_to='image/%Y%m', verbose_name='图片'),
        ),
    ]
