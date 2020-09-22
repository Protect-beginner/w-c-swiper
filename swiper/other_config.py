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
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'}
    }
}

# 腾讯云配置
TENCENT_SECERT_ID = "AKIDjt2vXsAc2GOkpdpMq43yzjiQ5QYGcvvb"
TENCENT_SECERT_KEY = "kEdBdpnVxJOUFm33oOr3xoNgiW2Sbx4u"
TENCENT_CITY = "ap-guangzhou"
TENCENT_APPID = "1400405740"
TENCENT_SIGN = "Outlierwu"
TENCENT_TEMPLATEID = "677320"

