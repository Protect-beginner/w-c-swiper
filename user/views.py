from django.shortcuts import render
import random

import redis

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from common.tencent.sms import send_message
from user.models import UserModel, UserConfig
from user.serializers.account import FetchSerializer, SubmitSerializer, LoginSerializer, UserConfigSerializer


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
    '''登录或注册'''

    def post(self, request):
        ser = SubmitSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        phonenum = ser.validated_data.get("phonenum")
        res = UserModel.objects.filter(phonenum=phonenum).first()
        conn = redis.Redis(host="127.0.0.1", port=6379, db=0)
        if not res:
            dic = {
                "phonenum": phonenum,
                "nickname": phonenum,
                "gender": 1,
                "birthday": "2000-01-01",
                "location": "上海市宝山区",
            }
            user = UserModel.objects.create(phonenum=phonenum, nickname=phonenum)
            UserConfig.objects.create()
            conn.set("loginer", user.id)
            return Response({"code": 0, "data": dic})
        serializer = LoginSerializer(instance=res)
        conn.set("loginer", serializer.data.get("id"))
        return Response({"code": 0, "data": serializer.data})


class ProfileShowView(APIView):
    def get(self, request):
        conn = redis.Redis(host="127.0.0.1", port=6379, db=0)
        userid = int(conn.get("loginer").decode("utf8"))
        res = UserConfig.objects.get(pk=userid)
        serializer = UserConfigSerializer(instance=res)
        return Response({"code": 0, "data": serializer.data})
