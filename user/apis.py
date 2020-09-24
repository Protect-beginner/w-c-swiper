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
        return Response({"code": 0, "data": None})


class SubmitView(APIView):
    '''登录或注册'''

    def post(self, request):
        ser = SubmitSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        phonenum = ser.validated_data.get("phonenum")
        try:
            # 有则登录，无的注册
            user = UserModel.objects.get(phonenum=phonenum)
        except UserModel.DoesNotExist:
            user = UserModel.objects.create(phonenum=phonenum, nickname=phonenum)
        request.session["uid"] = user.id
        serializer = LoginSerializer(instance=user)
        return Response({"code": 0, "data": serializer.data})


class ProfileShowView(APIView):
    '''查看用户配置'''

    def get(self, request):
        userid = request.session.get("uid")
        _res, _ = UserConfig.objects.get_or_create(id=userid)
        serializer = UserConfigSerializer(instance=_res)
        return Response({"code": 0, "data": serializer.data})


class ProfileUpdateView(APIView):
    '''修改用户配置'''

    def post(self, request):
        datas = request.data

        user_serializer = LoginSerializer(data=datas)
        config_serializer = UserConfigSerializer(data=datas)
        is_user_serializer = user_serializer.is_valid()
        is_config_serializer = config_serializer.is_valid()

        if is_user_serializer and is_config_serializer:
            userid = request.session.get("uid")
            UserModel.objects.filter(id=userid).update(**user_serializer.validated_data)
            UserConfig.objects.update_or_create(id=userid, defaults=config_serializer.validated_data)
            return Response({"code": 0, "data": None})
        else:
            res = {}
            res.update(user_serializer.errors)
            res.update(config_serializer.errors)
            return Response({"code": 1003, "data": res})
