from datetime import datetime
from django.db import models
from users.models import UserProfile
from paper.models import Paper

# Create your models here.


class PaperComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户", help_text='用户')
    papers = models.ForeignKey(Paper, verbose_name="试卷", help_text='试卷')
    comments = models.CharField(max_length=200, verbose_name="评论", help_text='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name


class UserLike(models.Model):
    users = models.ForeignKey(UserProfile, verbose_name="用户", help_text='用户')
    like_id = models.IntegerField(default=0, verbose_name="数据id", help_text='数据id')
    like_type = models.IntegerField(choices=((1, "类型"), (2, "试卷")), default=2, verbose_name="收藏类型"
                                    , help_text='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="接受用户", help_text='接受用户')
    message = models.CharField(max_length=400, verbose_name="消息内容", help_text='消息内容')
    if_read = models.BooleanField(default=False, verbose_name="是否已读", help_text='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserPaper(models.Model):
    users = models.ForeignKey(UserProfile, verbose_name="用户", help_text='用户')
    papers = models.ForeignKey(Paper, verbose_name="试卷", help_text='试卷')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = "已做信息"
        verbose_name_plural = verbose_name

