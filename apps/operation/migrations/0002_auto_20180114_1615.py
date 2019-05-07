# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 16:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papercomment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='papercomment',
            name='comments',
            field=models.CharField(help_text='评论', max_length=200, verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='papercomment',
            name='papers',
            field=models.ForeignKey(help_text='试卷', on_delete=django.db.models.deletion.CASCADE, to='paper.Paper', verbose_name='试卷'),
        ),
        migrations.AlterField(
            model_name='papercomment',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='userlike',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userlike',
            name='like_id',
            field=models.IntegerField(default=0, help_text='数据id', verbose_name='数据id'),
        ),
        migrations.AlterField(
            model_name='userlike',
            name='like_type',
            field=models.IntegerField(choices=[(1, '试卷'), (2, '题目')], default=2, help_text='收藏类型', verbose_name='收藏类型'),
        ),
        migrations.AlterField(
            model_name='userlike',
            name='users',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='if_read',
            field=models.BooleanField(default=False, help_text='是否已读', verbose_name='是否已读'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(help_text='消息内容', max_length=400, verbose_name='消息内容'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.IntegerField(default=0, help_text='接受用户', verbose_name='接受用户'),
        ),
        migrations.AlterField(
            model_name='userpaper',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userpaper',
            name='papers',
            field=models.ForeignKey(help_text='试卷', on_delete=django.db.models.deletion.CASCADE, to='paper.Paper', verbose_name='试卷'),
        ),
        migrations.AlterField(
            model_name='userpaper',
            name='users',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
