import random

from common.cache import rds

from common.tencent.sms import send_message


def rand_code(lenth=6):
    '''产生指定长度的验证码'''
    vcode = ''.join([str(random.randint(0, 9)) for i in range(lenth)])
    return vcode


def send_msg(phone):
    '''发送短信'''
    # 这里不同的模块存入缓存中要设置不同的前缀key
    key = 'Vcode-%s' % phone
    # 防止用户短时间多次发送信息
    if rds.get(key):
        print(rds.get(key), "++++++")
        return True
    vcode = rand_code()
    print(vcode)
    rds.set(key, vcode, 600)
    # return send_message(phone, vcode)
    return True
