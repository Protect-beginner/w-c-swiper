from django.db import models


class UserInfo(models.Model):
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    phonenum = models.IntegerField(max_length=11, verbose_name='手机号')
    birthday = models.DateTimeField(verbose_name='生日', default=2020 - 1 - 1)
    gender = models.BooleanField(verbose_name='性别', default='1')
    location = models.CharField(max_length=128, verbose_name='常居地', default='中国')

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return self.nickname
