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



