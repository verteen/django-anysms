# -*- coding: utf-8 -*-

from django.db import models


class MessageState(models.Model):
    name = models.CharField(max_length=50)


class Message(models.Model):
    phone = models.CharField(max_length=255, db_index=True)
    text = models.CharField(max_length=800)
    state = models.ForeignKey(MessageState, null=True, default=None, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
