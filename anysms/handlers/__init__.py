# -*- coding: utf-8 -*-


def get_handler(name):
    i = __import__("anysms.handlers.%s" % name, fromlist=["anysms.handlers"])
    return i.Handler()