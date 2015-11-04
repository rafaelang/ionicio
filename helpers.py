import urllib2
import base64
import json

class IonicPush(object):

    url = 'https://push.ionic.io/api/v1/'

    @classmethod
    def config(cls, app_id, private_key):
        cls.app_id = app_id
        cls.private_key = private_key
        b64 = base64.encodestring('%s:' % private_key).replace('\n', '')
        cls.auth = "Basic %s" % b64

    @classmethod
    def _set_headers(cls):
        cls.req.add_header("Content-Type", "application/json")
        cls.req.add_header("X-Ionic-Application-Id", cls.app_id)
        cls.req.add_header("Authorization", cls.auth)

    @classmethod
    def send(cls, tokens, msg, **kwargs):
        push_dict = {}
        notification_dict = {}
        push_dict["tokens"] = tokens
        notification_dict["alert"] = msg
        push_dict["notification"] = notification_dict
        push_dict["production"] = kwargs.get('production', True)

        push_dict = json.dumps(push_dict)

        cls.req = urllib2.Request(cls.url+'push/', data=push_dict)
        cls._set_headers()

        return urllib2.urlopen(cls.req)

    @classmethod
    def check_message(cls, id):
        cls.req = urllib2.Request(cls.url+'status/'+id)
        cls._set_headers()
        return urllib2.urlopen(cls.req)