import base64
import requests

class IonicPush(object):

    url = 'https://push.ionic.io/api/v1/'

    @classmethod
    def config(cls, app_id, private_key):
        cls.app_id = app_id
        cls.private_key = private_key
        b64 = base64.encodestring('%s:' % private_key).replace('\n', '')
        cls.auth = "Basic %s" % b64

    @classmethod
    def get_headers(cls):
        return {"Content-Type": "application/json",
            "X-Ionic-Application-Id": cls.app_id,
            "Authorization": cls.auth}

    @classmethod
    def send(cls, tokens, msg, **kwargs):
        push_dict = {}
        notification_dict = {}
        push_dict["tokens"] = tokens
        notification_dict["alert"] = msg
        push_dict["notification"] = notification_dict
        push_dict["production"] = kwargs.get('production', True)

        return requests.post(cls.url+'push/', json=push_dict, headers=cls.get_headers())

    @classmethod
    def check_message(cls, id):
        return requests.get(cls.url+'status/'+id, headers=cls.get_headers())
