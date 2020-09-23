import redis

from django.core.cache import cache

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import UserModel, UserConfig
from user.serializers.validataors import check_phone


class FetchSerializer(serializers.Serializer):
    '''发送短信序列化器'''
    phonenum = serializers.CharField(label="手机号", validators=[check_phone, ])


class SubmitSerializer(serializers.Serializer):
    '''登录/注册序列化器1'''
    phonenum = serializers.CharField(label="手机号", validators=[check_phone, ])
    vcode = serializers.CharField(label="验证码")

    def validate_vcode(self, vcode):
        if len(vcode) != 6:
            raise ValidationError("验证码位数错误")
        if not vcode.isdecimal():
            raise ValidationError("验证码格式错误")
        phonenum = self.initial_data.get("phonenum")
        key = "Vcode-%s" % phonenum
        res = cache.get(key)
        if not res:
            raise ValidationError("验证码失效")
        if res != vcode:
            raise ValidationError("验证码错误")
        return vcode


class LoginSerializer(serializers.ModelSerializer):
    '''登录/注册序列化器2'''
    class Meta:
        model = UserModel
        fields = "__all__"


class UserConfigSerializer(serializers.ModelSerializer):
    '''用户配置序列化器'''
    class Meta:
        model = UserConfig
        fields = "__all__"
