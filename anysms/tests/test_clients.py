# -*- coding: utf-8 -*-
from django.test import TestCase
from anysms.clients import smsc_api
from django.conf import settings


class SmscApiTests(TestCase):
    def setUp(self):
        configs = settings.SMS_HANDLERS['smsc_ru']

        self.api = smsc_api.SMSC(login=configs['login'], password=configs['password'], options={'debug': True})

    def test_send(self):
        options = {'cost': 1}
        r = self.api.send('79161234500', 'test', options)
        self.assertTrue(r.get('cnt') and r.get('cost'), msg=str(r))

    def test_balance(self):
        r = self.api.balance()
        self.assertTrue(r.get('balance'))

    def test_status(self):
        r = self.api.status('79161234500', 1)
        self.assertTrue(r.get('error'))

    def test_phones(self):
        r1 = self.api.phones({'add_group': 1, 'name': 'test'})
        self.assertTrue(r1.get('id'))
        r2 = self.api.phones({'del_group': 1, 'grp': r1.get('id')})
        self.assertTrue(r2.get('result') == 'OK')

    # todo test other methods


