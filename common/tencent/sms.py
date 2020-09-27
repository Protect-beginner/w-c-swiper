from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models

from swiper import other_config

def send_message(phone,random_code):
    try:
        cred = credential.Credential(other_config.TENCENT_SECERT_ID, other_config.TENCENT_SECERT_KEY)
        client = sms_client.SmsClient(cred, other_config.TENCENT_CITY, )
        req = models.SendSmsRequest()
        req.SmsSdkAppid = other_config.TENCENT_APPID
        req.Sign = other_config.TENCENT_SIGN
        req.PhoneNumberSet = ["+86" + phone]
        req.TemplateID = other_config.TENCENT_TEMPLATEID
        req.TemplateParamSet = [str(random_code), ]
        resp = client.SendSms(req)

        if resp.SendStatusSet[0].Code == "Ok":
            return True
        print(resp.to_json_string(indent=2))

    except TencentCloudSDKException as err:
        print(err)