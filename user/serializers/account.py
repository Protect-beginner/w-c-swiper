import redis
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import UserModel
from user.serializers.validataors import check_phone


class FetchSerializer(serializers.Serializer):
    '''发送短信序列化器'''
    phonenum = serializers.CharField(label="手机号", validators=[check_phone, ])


class SubmitSerializer(serializers.Serializer):
    '''登录/注册序列化器'''
    phonenum = serializers.CharField(label="手机号", validators=[check_phone, ])
    vcode = serializers.CharField(label="验证码")

    def validate_vcode(self, vcode):
        if len(vcode) != 6:
            raise ValidationError("验证码位数错误")
        if not vcode.isdecimal():
            raise ValidationError("验证码格式错误")
        conn = redis.Redis(host="127.0.0.1", port=6379, db=0)
        phonenum = self.initial_data.get("phonenum")
        res = conn.get(phonenum)
        if not res:
            raise ValidationError("验证码失效")
        if res.decode("utf8") != vcode:
            raise ValidationError("验证码错误")
        return vcode


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
