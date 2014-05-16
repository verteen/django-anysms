# -*- coding: utf-8 -*-

import abc
from anysms.models import Message


class BaseHandler(object):
    __metaclass__ = abc.ABCMeta

    def send(self, phone, text):
        msg = Message(phone=phone, text=text)
        return self.api_request('send', msg)

    @abc.abstractmethod
    def api_request(self, method, data):
        """
        Please Implement this method
        """
        return


