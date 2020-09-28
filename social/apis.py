from common.http import rend_json
from social.logics import rcmd
from social.logics import like_someone
from social.logics import super_like_someone
from social.logics import dislike_someone


def rcmd_users(request):
    '''滑动记录'''
    uid = request.session["uid"]
    users_data = [users.to_dict() for users in rcmd(uid)]
    return rend_json(data=users_data)


def like(request):
    '''喜欢某人'''
    uid = request.session["uid"]
    sid = int(request.POST.get("sid"))
    res = like_someone(uid, sid)
    return rend_json(data={"is_matched": res})


def super_like(request):
    '''超级喜欢某人'''
    uid = request.session["uid"]
    sid = int(request.POST.get("sid"))
    res = super_like_someone(uid, sid)
    return rend_json(data={"is_matched":res})


def dislike(request):
    uid = request.session["uid"]
    sid = int(request.POST.get("sid"))
    res = dislike_someone(uid, sid)
    return rend_json()