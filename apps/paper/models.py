from datetime import datetime
from django.db import models

# Create your models here.


class Type(models.Model):

    TYPE_S = (
        (1, '一级目录'),
        (2, '二级目录'),
    )

    name = models.CharField(default='', max_length=10, verbose_name="类型名", help_text='类型名')
    code = models.CharField(default='', max_length=10, verbose_name='类型code', help_text='类型code')
    instr = models.TextField(max_length=300, verbose_name="介绍", help_text="介绍")
    click = models.IntegerField(default=0, verbose_name="点击人数", help_text="点击人数")
    type_s = models.IntegerField(default=0, choices=TYPE_S, verbose_name='类目级别', help_text='类目级别')
    image = models.ImageField(upload_to="type/%Y/%m", verbose_name="类型图片", help_text="类型图片")
    parents = models.ForeignKey('self', null=True, blank=True, verbose_name='父类目级别', help_text='父类目级别',
                                related_name='sub_types')
    is_parents = models.BooleanField(default='False', verbose_name='是否为父级目录')
    is_tab = models.BooleanField(default='False', verbose_name='是否导航', help_text='是否导航')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')

    class Meta:
        verbose_name = "试卷类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Paper(models.Model):
    types = models.ForeignKey(Type, null=True, blank=True, verbose_name="试卷", help_text='试卷')
    name = models.CharField(max_length=20, verbose_name="试卷名称", help_text='试卷名称')
    num = models.IntegerField(default=0, verbose_name="题目数量", help_text='题目数量')
    level = models.CharField(choices=(("easy", "简单"), ("middle", "中等"), ("hard", "困难")), max_length=10,
                             verbose_name='难度', help_text='难度')
    student = models.IntegerField(default=0, verbose_name="已做人数", help_text='已做人数')
    like = models.IntegerField(default=0, verbose_name="收藏人数", help_text='收藏人数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = "试卷"
        verbose_name_plural = verbose_name


class Topic(models.Model):
    papers = models.ForeignKey(Paper, null=True, blank=True, verbose_name="题目", help_text='题目')
    name = models.CharField(max_length=300, verbose_name="题目内容", help_text='题目内容')
    answer = models.CharField(max_length=4, verbose_name="标准答案", help_text='标准答案')
    num = models.CharField(max_length=2, default=0, verbose_name="题目num", help_text='题目num')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = "题目"
        verbose_name_plural = verbose_name


class Answer(models.Model):
    topics = models.ForeignKey(Topic, null=True, blank=True, related_name="topics", verbose_name="答案", help_text='答案')
    content = models.CharField(max_length=50, verbose_name="内容", help_text='内容')
    value = models.CharField(max_length=2, choices=(("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")), default="A",
                             verbose_name='选项')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = "答案"
        verbose_name_plural = verbose_name