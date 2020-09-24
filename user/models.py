from django.db import models


class UserInfo(models.Model):
    '''User模型'''

    GENDERS = (
        ('male', '男'),
        ('female', '女')
    )

    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ("武汉", "武汉"),
        ("沈阳", "沈阳"),
    )
    nickname = models.CharField(max_length=32, db_index=True, verbose_name='昵称')
    phonenum = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    birthday = models.DateTimeField(default='2002-01-01', verbose_name='生日')
    gender = models.CharField(max_length=8, choices=GENDERS, verbose_name='性别', default='男')
    location = models.CharField(max_length=32, choices=LOCATIONS, verbose_name='常居地', default='北京')
    avatar = models.CharField(max_length=256, default='q', verbose_name='头像')

    class Meta:
        db_table = 'userinfo'

    def __str__(self):
        return self.nickname
