import datetime

from social.models import Swiped
from social.models import Friend
from user.models import UserModel
from user.models import UserConfig

from common.cache import rds
from common.keys import FIRST_RCMD_Q


def rcmd_from_rds(uid):
    '''从推荐队列获取推荐用户'''
    user_lists = rds.lrange(FIRST_RCMD_Q % uid, 0, 19)
    user_list = [int(user) for user in user_lists]
    return UserModel.objects.filter(id__in=user_list)


def rcmd_from_db(uid, num=20):
    '''从数据库获取推荐用户'''
    profile = UserConfig.objects.get(id=uid)
    # 推荐年龄
    now = datetime.date.today()
    earliest_birth = now - datetime.timedelta(profile.max_dating_age * 365)
    latest_birth = now - datetime.timedelta(profile.min_dating_age * 365)

    # 取出该用户所有的滑动记录的sid,将其排除  flat使其扁平化[(1,),(2,)] -> [1,2]
    sid_list = Swiped.objects.filter(uid=uid).values_list("sid", flat=True)

    user = UserModel.objects.filter(
        gender=profile.dating_gender,
        location=profile.dating_location,
        birthday__range=[earliest_birth, latest_birth]
    ).exclude(id__in=sid_list)[:num]
    return user


def rcmd(uid):
    '''推荐用户'''
    # 获取优先队列推荐用户队列
    fist_users = rcmd_from_rds(uid)
    # 获取数据库推荐用户队列
    num = 20 - len(fist_users)
    if num:
        second_users = rcmd_from_db(uid, num)
        return set(fist_users) | set(second_users)
    else:
        return fist_users


def like_someone(uid, sid):
    '''喜欢某人(右滑)'''
    # 添加滑动记录
    Swiped.swiper(uid=uid, sid=sid, mark="like")
    # 双方喜欢则配对成好友
    if Swiped.is_liked(uid, sid) is True:
        Friend.objects.create(uid1=uid, uid2=sid)
        return True
    else:
        return False


def super_like_someone(uid, sid):
    '''超级喜欢某人(上滑)'''
    Swiped.swiper(uid=uid, sid=sid, mark="superlike")
    # 超级喜欢会优先推荐(推荐队列)
    rds.lpush(FIRST_RCMD_Q % sid, uid)
    if Swiped.is_liked(uid, sid) is True:
        Friend.objects.create(uid1=uid, uid2=sid)
        return True
    else:
        return False


def dislike_someone(uid, sid):
    '''不喜欢某人(左滑)'''
    Swiped.swiper(uid=uid, sid=sid, mark="dislike")
    # 强制从优先推荐队列中删除
    rds.lrem(FIRST_RCMD_Q % uid, count=0, value=sid)
