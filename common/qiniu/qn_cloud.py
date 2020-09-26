import time
import json
from swiper import other_config as oc
from qiniu import Auth


def get_res_url(filename):
    return f"http://{oc.QN_CALLBACK_DOMAIN}/{filename}"


def gen_token(uid, filename):
    policy = {
        "scope": oc.QN_BUCKET,
        "deadline": int(time.time() + 600),
        "endUser": 1,
        "returnBody": json.dumps({'code': 0, 'data': get_res_url(filename)}),
        "callbackUrl": oc.QN_CALLBACK_URL,
        "callbackHost": oc.QN_CALLBACK_DOMAIN,
        "callbackBody": f"key={filename}&uid={uid}",
        "saveKey": filename,
        'forceSaveKey': True,
        'fsizeLimit': 10485760,  # 文件大小的最大值: 10 MB
        'mimeLimit': 'image/*',
    }
    qn_auth = Auth(oc.QN_ACCESS_KEY, oc.QN_SECRET_KEY)

    token = qn_auth.upload_token(oc.QN_BUCKET, filename, 600, policy)
    return token
