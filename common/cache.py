# 自定义redis
from redis import Redis as _Redis
import pickle
from pickle import UnpicklingError
from swiper.other_config import REDIS


class Redis(_Redis):
    '''带序列化处理的 set 方法'''
    def set(self, name, value, ex=None, px=None, nx=False, xx=False, keepttl=False):
        bin_data = pickle.dumps(value, pickle.HIGHEST_PROTOCOL)
        return super().set(name, bin_data, ex, px, nx, xx, keepttl)

    '''带序列化处理的 get 方法'''
    def get(self, name, default=None):
        pickle_data = super().get(name)
        if pickle_data is None:
            return default
        try:
            value = pickle.loads(pickle_data)
        except (KeyError,EOFError,UnpicklingError):
            return pickle_data
        else:
            return value
# 设置一个全局变量实现一个简单的单例模式
rds = Redis(**REDIS)