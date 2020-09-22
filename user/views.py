from django.shortcuts import render
import random
import re

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from common.tencent.sms import send_message


class FetchView(APIView):
    '''提交手机号'''

    def get(self, request):
        phonenum = request.query_params.get("phonenum")
        if not re.match(r'^(1[3|5|6|7|8|9])\d{9}$', phonenum):
            raise ValidationError("手机号格式错误")
        vcode = random.randint(100000, 999999)
        send_message(phonenum, vcode)
        print(vcode)
        return Response({"code": 0, "data": ""})


class SubmitView(APIView):
    '''登录或注册'''

    def post(self, request):
        phonenum = request.data.get("phonenum")
        vcode = request.data.get("vcode")
