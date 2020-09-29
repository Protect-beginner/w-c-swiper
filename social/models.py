from django.db import models


class Swiped(models.Model):
    '''划过的记录'''
    MARKTYP = (
        ("like", "喜欢"),
        ("superlike", "超级喜欢"),
        ("dislike", "不喜欢")
    )
    uid = models.IntegerField(verbose_name="⽤户⾃身id")
    sid = models.IntegerField(verbose_name="被滑的陌⽣⼈id")
    mark = models.CharField(max_length=10, choices=MARKTYP, verbose_name="滑动类型")
    time = models.DateTimeField(auto_now_add=True, verbose_name="滑动的时间")

    class Meta:
        unique_together = ["uid", "sid"]  # 联合唯一

    @classmethod
    def swiper(cls, uid, sid, mark):
        ''''''
        cls.objects.create(uid=uid, sid=sid, mark=mark)

    @classmethod
    def is_liked(cls, uid, sid):
        '''是否喜欢'''
        _swiper = cls.objects.filter(uid=sid, sid=uid).first()
        if not _swiper:  # 未滑动过
            return None
        elif _swiper.mark in ["like", "superlike"]:
            return True
        else:
            return False


class Friend(models.Model):
    '''匹配到的好友'''
    uid1 = models.IntegerField(verbose_name="uid1")
    uid2 = models.IntegerField(verbose_name="uid2")

    class Meta:
        unique_together = ["uid1", "uid2"]

    @classmethod
    def make_friends(cls, uid1, uid2):
        '''创建好友关系'''
        uid1, uid2 = (uid2, uid1) if uid1 > uid2 else (uid1, uid2)  # 调整两者位置
        return cls.objects.create(uid1=uid1, uid2=uid2)

    @classmethod
    def break_out(cls, uid1, uid2):
        uid1, uid2 = (uid2, uid1) if uid1 > uid2 else (uid1, uid2)
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()
