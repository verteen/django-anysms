# -*- coding: utf-8 -*-

from anysms.handlers.common import BaseHandler

from anysms.clients import smsc_api
from django.conf import settings

configs = settings.SMS_HANDLERS['smsc_ru']


class Handler(BaseHandler):
    name = 'smsc_ru'

    api = smsc_api.SMSC(login=configs['login'], password=configs['password'], sender=configs.get('sender'))

    def api_request(self, method, data):
        if method == 'send':
            resp = self.api.send(phone=data.phone, message=data.text, )
            data.save()
            return resp

