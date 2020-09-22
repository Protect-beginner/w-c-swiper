from django.db import models


class UserModel(models.Model):
    phonenum = models.CharField(max_length=11, unique=True, null=False, blank=False, verbose_name="手机号",
                                help_text="手机号")
    nickname = models.CharField(max_length=32, verbose_name="昵称", help_text="昵称")
    gender = models.BooleanField(choices=((1, "male"), (0, "female")), default=1, verbose_name="性别", help_text="性别")
    birthday = models.DateField(verbose_name="生日", help_text="生日", default="2020-01-01")
    # avatar = models.CharField()
    location = models.CharField(max_length=64, verbose_name="常居地", help_text="常居地", default="上海市宝山区")

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phonenum
