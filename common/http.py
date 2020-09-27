import json
from django.conf import settings
from django.http import HttpResponse


def rend_json(data=None, code=0):
    '''将数据渲染成 JSON 数据'''
    result = {
        "code": code,
        "data": data,
    }
    if settings.DEBUG is True:
        json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = json.dumps(result, ensure_ascii=False, separators=(',', ':'))
    response = HttpResponse(content=json_str, content_type="application/json")
    return response
