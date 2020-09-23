import redis

from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.views import APIView

from user.logics import send_msg
from user.models import UserModel, UserConfig
from user.serializers.account import FetchSerializer, SubmitSerializer, LoginSerializer, UserConfigSerializer


class FetchView(APIView):
    '''提交手机号'''

    def get(self, request):
        # 不能直接传入request.query_params.get("phonenum"),要传入字典
        res = FetchSerializer(data=request.query_params)
        res.is_valid(raise_exception=True)
        phonenum = res.validated_data.get("phonenum")
        send_msg(phonenum)
        return Response({"code": 0, "data": ""})


class SubmitView(APIView):
    '''登录或注册'''

    def post(self, request):
        ser = SubmitSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        phonenum = ser.validated_data.get("phonenum")
        res = UserModel.objects.filter(phonenum=phonenum).first()
        if not res:
            user = UserModel.objects.create(phonenum=phonenum, nickname=phonenum)
            UserConfig.objects.create()
            request.session['uid'] = user.id
            serializer = LoginSerializer(instance=user)
            return Response({"code": 0, "data": serializer.data})
        serializer = LoginSerializer(instance=res)
        request.session['uid'] = res.id
        return Response({"code": 0, "data": serializer.data})


class ProfileShowView(APIView):
    '''查看用户配置'''

    def get(self, request):
        userid = request.session.get("uid")
        res = UserConfig.objects.get(pk=userid)
        serializer = UserConfigSerializer(instance=res)
        return Response({"code": 0, "data": serializer.data})


class ProfileUpdateView(APIView):
    '''修改用户配置'''

    def post(self, request):
        conn = redis.Redis(host="127.0.0.1", port=6379, db=0)
        userid = int(conn.get("loginer").decode("utf8"))
        user = UserConfig.objects.get(pk=userid)
        print(user.max_distance)
        res = request.data
        for key in res:
            # print(key)
            user.key = res.key
        # user.save()
        return Response({"code": 0, "data": ""})

