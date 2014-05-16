# -*- coding: utf-8 -*-

import requests

RESPONSE_FORMAT_STR = 0  # – (по умолчанию) в виде строки (OK - 1 SMS, ID - 1234).
RESPONSE_FORMAT_SET = 1  # – вернуть ответ в виде чисел: ID и количество SMS через запятую (1234,1), при cost = 2 еще стоимость через запятую (1234,1,1.40), при cost = 3 еще новый баланс Клиента (1234,1,1.40,100.50), при cost = 1 стоимость и количество SMS через запятую (1.40,1).
RESPONSE_FORMAT_XML = 2  # – ответ в xml формате.
RESPONSE_FORMAT_JSON = 3  # – ответ в json формате.

SERVICE_URL = '//smsc.ru/sys/'

API_METHODS = {
    'send': 'send.php',  # http://smsc.ru/api/http/#send
    'balance': 'balance.php',  # http://smsc.ru/api/http/#bal
    'status': 'status.php',  # http://smsc.ru/api/http/#status
    'phones': 'phones.php',  # http://smsc.ru/api/http/#contact
    'users': 'users.php',  # http://smsc.ru/api/http/#subclient
    'info': 'info.php',  # http://smsc.ru/api/http/#operator
    'get': 'get.php',  # http://smsc.ru/api/http/#sender
    'receive_phones': 'receive_phones.php',  # http://smsc.ru/api/http/#receive
    'senders': 'senders.php',  # http://smsc.ru/api/http/#senders
}


class SMSC(object):
    def __init__(self, login, password, sender=None, options=None):
        self.default_payload = {
            'login': login,
            'psw': password,
            'sender': sender,
            'fmt': 3,
        }
        if options:
            self.options = options
        else:
            self.options = {'post': True, 'debug': False, 'https': False}

    def api_request(self, method, data):
        proto = 'https:' if self.options.get('https') else 'http:'
        url = proto + SERVICE_URL + API_METHODS.get(method)

        payload = dict(self.default_payload)
        payload.update(data)

        if self.options.get('post'):
            response = requests.post(url, data=payload)
        else:
            response = requests.get(url, params=payload)

        if self.options.get('debug'):
            print('service url: %s' % url)
            print('request url: %s' % response.url)
            print('response: %s' % response.text)

        if payload.get('fmt') == 3:
            try:
                result = response.json()
            except ValueError:
                result = {'result': response.text}
        else:
            result = response.text

        return result

    def send(self, phone, message, options=None):
        data = {'phones': phone, 'mes': message}
        if options:
            data.update(options)
        return self.api_request('send', data)

    def balance(self):
        return self.api_request('balance', {})

    def status(self, phone, message_id, options=None):
        data = {'phone': phone, 'id': message_id}
        if options:
            data.update(options)
        return self.api_request('status', data)

    def phones(self, data):
        return self.api_request('phones', data)

    def users(self, data):
        return self.api_request('users', data)

    def info(self, phone):
        data = {'phone': phone, 'get_operator': 1}
        return self.api_request('info', data)

    def get(self, data):
        return self.api_request('get', data)

    def receive_phones(self, data):
        return self.api_request('receive_phones', data)

    def senders(self, data):
        return self.api_request('senders', data)









