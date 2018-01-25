import requests
import json
__version__ = '0.0.1'

class Jsms(object):

    BASE_URL = 'https://api.sms.jpush.cn/v1/'

    def __init__(self, app_key, master_secret):
        self.session = requests.Session()
        self.session.auth = (app_key, master_secret)

    def send_code(self, mobile, temp_id):
        body = {
            'mobile': mobile,
            'temp_id': temp_id
        }
        return self._post('codes', body)

    def send_voice_code(self, mobile, code=None, lang=None, ttl=None):
        body = {
            'mobile': mobile
        }
        if code is not None:
            body['code'] = code
        if lang is not None:
            body['voice_lang'] = lang
        if ttl is not None:
            body['ttl'] = ttl
        return self._post('voice_codes', body)

    def verify_code(self, msg_id, code):
        end_point = 'codes/' + msg_id + '/valid'
        body = {
            'code': code
        }
        return self._post(end_point, body)

    def send_teml(self, mobile, temp_id, temp_para=None, time=None):
        body = {
            'mobile': mobile,
            'temp_id': temp_id
        }
        if temp_para is not None:
            body['temp_para'] = temp_para
        if time is not None:
            body['time'] = time
        return self._post('messages', body)


    def send_batch_teml(self, mobile, temp_id, recipients=None):
        pass

    def show_schedule_message(self, schedule_id):
        end_point = 'schedule/' + schedule_id
        return self._get(end_point)

    def update_schedule_message(self, schedule_id, mobile, temp_id, temp_para=None, time=None):
        pass

    def delete_schedule_message(self, schedule_id):
        end_point = 'schedule/' + schedule_id
        return self._del(end_point)

    def app_balance(self):
        end_point = 'accounts/app'
        return self._get(end_point)

    def _get(self, end_point):
        return self._request('GET', end_point)

    def _del(self, end_point):
        return self._request('DELETE', end_point)

    def _post(self, end_point, body):
        return self._request('POST', end_point, body)

    def _request(self, method, end_point, body):
        uri = self.BASE_URL + end_point
        r = self.session.request(method, uri, data=json.dumps(body))
        print(r.json())

