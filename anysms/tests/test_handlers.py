# -*- coding: utf-8 -*-
from django.test import TestCase
from anysms.handlers import get_handler

class GetHandlerTests(TestCase):
    def test_get_handler(self):
        hnd = get_handler('smsc_ru')
        self.assertEqual(hnd.name, 'smsc_ru')