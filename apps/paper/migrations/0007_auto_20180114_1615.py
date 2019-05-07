# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 16:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_auto_20180114_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(help_text='内容', max_length=50, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='topics',
            field=models.ForeignKey(blank=True, help_text='答案', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='paper.Topic', verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='level',
            field=models.CharField(choices=[('easy', '简单'), ('middle', '中等'), ('hard', '困难')], help_text='难度', max_length=10, verbose_name='难度'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='like',
            field=models.IntegerField(default=0, help_text='收藏人数', verbose_name='收藏人数'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='name',
            field=models.CharField(help_text='试卷名称', max_length=20, verbose_name='试卷名称'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='num',
            field=models.IntegerField(default=0, help_text='题目数量', verbose_name='题目数量'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='student',
            field=models.IntegerField(default=0, help_text='已做人数', verbose_name='已做人数'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='types',
            field=models.ForeignKey(blank=True, help_text='试卷', null=True, on_delete=django.db.models.deletion.CASCADE, to='paper.Type', verbose_name='试卷'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='answer',
            field=models.CharField(help_text='标准答案', max_length=4, verbose_name='标准答案'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(help_text='题目内容', max_length=300, verbose_name='题目内容'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='papers',
            field=models.ForeignKey(blank=True, help_text='题目', null=True, on_delete=django.db.models.deletion.CASCADE, to='paper.Paper', verbose_name='题目'),
        ),
        migrations.AlterField(
            model_name='type',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
    ]
