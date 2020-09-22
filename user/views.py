from django.shortcuts import render
import random

import redis

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from common.tencent.sms import send_message
from user.models import UserModel
from user.serializers.account import FetchSerializer, SubmitSerializer, LoginSerializer


class FetchView(APIView):
    '''提交手机号'''

    def get(self, request):
        # 不能直接传入request.query_params.get("phonenum"),要传入字典
        res = FetchSerializer(data=request.query_params)
        res.is_valid(raise_exception=True)
        vcode = random.randint(100000, 999999)
        print(vcode)
        phonenum = res.validated_data.get("phonenum")
        # send_message(phonenum, vcode)
        conn = redis.Redis(host="127.0.0.1", port=6379, db=0)
        conn.set(phonenum, vcode, ex=180)

        return Response({"code": 0, "data": ""})


class SubmitView(APIView):
    '''
    登录或注册
    1.获取手机号，验证码
    2.查看redis
        1.无手机号,报错
        2.验证码错误
        3.正确
    3.查看数据库
        1.有手机号，登录
        2.无手机号，注册
    '''

    def post(self, request):
        ser = SubmitSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        phonenum = ser.validated_data.get("phonenum")
        res = UserModel.objects.filter(phonenum=phonenum).first()
        if not res:
            dic = {
                "phonenum": phonenum,
                "nickname": phonenum,
                "gender": 1,
                "birthday": "2000-01-01",
                "location": "上海市宝山区",
            }
            UserModel.objects.create(phonenum=phonenum, nickname=phonenum)
            return Response({"code": 0, "data": dic})
        serializer = LoginSerializer(instance=res)
        return Response({"code": 0, "data": serializer.data})
