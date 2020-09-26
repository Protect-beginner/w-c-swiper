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
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/0',
#         'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'}
#     }
# }

# 七牛云配置
QN_DOMAIN = 'qh6tx5nfy.hd-bkt.clouddn.com'
QN_BUCKET = 'oulierwu'
QN_ACCESS_KEY = 'Pwm87MIIP6ePq-p_quhCjwvypkElsMlvduWeJ3DC'
QN_SECRET_KEY = 'Ex-aN47vta4fqpOCn5rvoqKBqqrTX-gev7r-XB-my'
QN_CALLBACK_URL = 'http://106.14.222.135/qiniu/callback'
QN_CALLBACK_DOMAIN = '106.14.222.135'


