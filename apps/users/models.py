from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="female",
                              verbose_name='性别', help_text='性别')
    mobile = models.CharField(max_length=11, verbose_name='手机号码', help_text='手机号码')
    image = models.ImageField(upload_to="image/%Y%m", default="image/default.jpg", max_length=100,
                              verbose_name='图片', help_text='图片')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(max_length=30, choices=(("register", "注册"), ("forget", "找回密码"),
                                                         ("update", "修改邮箱")), verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100, help_text='轮播图')
    url = models.URLField(max_length=200, verbose_name="访问地址", help_text='访问地址')
    index = models.IntegerField(default=100, verbose_name="顺序", help_text='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text='添加时间')

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name




