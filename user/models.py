from django.db import models


class UserModel(models.Model):
    '''用户'''
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ("武汉", "武汉"),
        ("沈阳", "沈阳")
    )
    phonenum = models.CharField(max_length=11, unique=True, null=False, blank=False, verbose_name="手机号",
                                help_text="手机号")
    nickname = models.CharField(max_length=32,db_index=True ,verbose_name="昵称", help_text="昵称")
    gender = models.CharField(max_length=16,choices=(("male", "男"), ("female", "女")), default="male", verbose_name="性别", help_text="性别")
    birthday = models.DateField(verbose_name="生日", help_text="生日", default="2020-01-01")
    # avatar = models.CharField(max_length=256,verbose_name="个人形象")
    location = models.CharField(choices=LOCATIONS,max_length=64, verbose_name="常居地", help_text="常居地", default="上海")

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phonenum


class UserConfig(models.Model):
    '''用户配置'''
    dating_gender = models.CharField(max_length=32,choices=(("male", "男"), ("female", "女")), default="male", verbose_name="性别",
                                        help_text="匹配性别")
    dating_location = models.CharField(max_length=64, verbose_name="目标城市", help_text="目标城市", default="上海市宝山区")
    max_distance = models.FloatField(verbose_name="最⼤查找范围", help_text="最⼤查找范围", default=20.0)
    min_distance = models.FloatField(verbose_name="最小查找范围", help_text="最小查找范围", default=1.0)
    max_dating_age = models.IntegerField(verbose_name="最⼤交友年龄", help_text="最⼤交友年龄", default=40)
    min_dating_age = models.IntegerField(verbose_name="最小交友年龄", help_text="最小交友年龄", default=20)
    vibration = models.BooleanField(choices=((1, "open"), (0, "close")), verbose_name="开启震动", help_text="开启震动",
                                    default=1)
    only_matched = models.BooleanField(verbose_name="不让未匹配的⼈看我的相册", help_text="不让未匹配的⼈看我的相册", default=1)
    auto_play = models.BooleanField(verbose_name="自动播放视频", help_text="自动播放视频", default=1)
    # user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "userconfig"
        verbose_name = "用户配置"
        verbose_name_plural = verbose_name
