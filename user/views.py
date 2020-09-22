import random
import uuid

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render

from django.views import View

from swiper.settings import EMAIL_HOST_USER
from user.models import UserInfo


class Userland(View):
    def get(self, request):
        phonenum = request.GET.get('phonenum')
        vcode = random.randint(0, 1000000)
        cache.set(vcode, [phonenum, vcode], 300)
        # 以uid为key，user为value存入缓存
        message = '验证码:{},-----5分钟内有效'.format(vcode)
        # 标题，内容，发邮件的邮箱，收邮件的邮箱，以html格式发邮箱
        send_mail('用户激活', message=message, from_email=EMAIL_HOST_USER,
                  recipient_list=[phonenum, ],
                  html_message=message)
        data = {
            'code': 0,
            'data': ''
        }
        return JsonResponse(data)

    def post(self, request):
        phonenum = request.POST.get('phonenum')
        vcode = request.POST.get('vcode')
        pv = cache.get(vcode)
        if pv == [phonenum, vcode]:
            user = UserInfo.objects.filter(phonenum=phonenum)
            if user:
                data = {
                    'code': 0,
                    'data': {
                        "id": user.id,
                        "nickname": user.nickname,
                        "phonenum": user.phonenum,
                        "birthday": user.birthday,
                        "gender": user.gender,
                        "location": user.location,
                    }
                }
                return JsonResponse(data)
            else:
                UserInfo.objects.create(
                    nickname=pv[0],
                    phonenum=pv[0],
                )
                user = UserInfo.objects.get(phonenum=phonenum)
                data = {
                    'code': 0,
                    'data': {
                        "id": user.id,
                        "nickname": user.nickname,
                        "phonenum": user.phonenum,
                        "birthday": user.birthday,
                        "gender": user.gender,
                        "location": user.location,
                    }
                }
                return JsonResponse(data)
        else:
            data = {
                'code': 1000,
                'data': '验证码错误'
            }
            return JsonResponse(data)
