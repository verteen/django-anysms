# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MessageState'
        db.create_table(u'sms_messagestate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'anysms', ['MessageState'])

        # Adding model 'Message'
        db.create_table(u'sms_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['anysms.MessageState'], null=True, on_delete=models.SET_NULL)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'anysms', ['Message'])


    def backwards(self, orm):
        # Deleting model 'MessageState'
        db.delete_table(u'sms_messagestate')

        # Deleting model 'Message'
        db.delete_table(u'sms_message')


    models = {
        u'anysms.message': {
            'Meta': {'object_name': 'Message'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['anysms.MessageState']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '800'})
        },
        u'anysms.messagestate': {
            'Meta': {'object_name': 'MessageState'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['anysms']