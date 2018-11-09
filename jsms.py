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
        end_point = 'messages'
        body = {
            'mobile': mobile,
            'temp_id': temp_id
        }
        if temp_para is not None:
            body['temp_para'] = temp_para
        if time is not None:
            body['send_time'] = time
            end_point = 'schedule'
        return self._post(end_point, body)


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

    def show_sign(self, sign_id):
        end_point = 'sign/' + sign_id
        return self._get(end_point)

    def delete_sign(self, sign_id):
        end_point = 'sign/' + sign_id
        return self._del(end_point)

    def create_sign(self, sign, image0=None, image1=None, image2=None, image3=None):
        end_point = 'sign'
        return self._sign(end_point, sign, image0, image1, image2, image3)

    def upadte_sign(self, sign_id, sign, image0=None, image1=None, image2=None, image3=None):
        end_point = 'sign/' + sign_id
        return self._sign(end_point, sign, image0, image1, image2, image3)

    def _sign(self, end_point, sign=None, image0=None, image1=None, image2=None, image3=None):
        uri = self.BASE_URL + end_point
        images = {
            'image0': image0,
            'image1': image1,
            'image2': image2,
            'image3': image3,
        }
        uploads = { k: v for k, v in images.items() if v is not None }
        uploads['sign'] = (None, sign)
        r = self.session.post(uri, files=uploads)
        if 0 == len(r.content):
            return r.status_code
        else:
            return r.json()

    def _get(self, end_point):
        return self._request('GET', end_point)

    def _del(self, end_point):
        return self._request('DELETE', end_point)

    def _post(self, end_point, body):
        return self._request('POST', end_point, body)

    def _request(self, method, end_point, body=None):
        uri = self.BASE_URL + end_point
        if body is not None:
            body = json.dumps(body)
        r = self.session.request(method, uri, data=body)
        if 0 == len(r.content):
            return r.status_code
        else:
            return r.json()
