# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'swiper',
        'USER': 'wu',
        'PASSWORD': '@19960518wyJ',
        'HOST': '106.14.222.135',
        'PORT': '3306',
    }
}
# redis设置
REDIS = {
    'host': 'localhost',
    'port': 63790,
    'db': 2,
}

#  腾讯云短信配置
TENCENT_SECERT_ID = "AKIDjt2vXsAc2GOkpdpMq43yzjiQ5QYGcvvb"
TENCENT_SECERT_KEY = "kEdBdpnVxJOUFm33oOr3xoNgiW2Sbx4u"
TENCENT_CITY = "ap-guangzhou"
TENCENT_APPID = "1400405740"
TENCENT_SIGN = "Outlierwu"
TENCENT_TEMPLATEID = "677320"

# 七牛云配置
QN_DOMAIN = 'qh6tx5nfy.hd-bkt.clouddn.com'
QN_BUCKET = 'outlierwu'
QN_ACCESS_KEY = 'Pwm87MIIP6ePq-p_quhCjwvypkElsMlvduWeJ3DC'
QN_SECRET_KEY = 'Ex-aN47vta4fqpOCn5rvoqKBqqrTX-gev7r-XB-m'
QN_CALLBACK_URL = 'http://106.14.222.135/qiniu/callback'
QN_CALLBACK_DOMAIN = '106.14.222.135'

# 反悔功能相关配置
REWIND_TIMES = 3         # 每日反悔次数
REWIND_TIMEOUT = 5 * 60  # 反悔超时时间

