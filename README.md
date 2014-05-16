django-anysms
=============

Django app for sending SMS


#install

###required
    Python 2.7+
    Django 1.6+
    requests 2.0+

###settings.py

 ```python
INSTALLED_APPS = (
    ...
    'anysms',
)

SMS_HANDLERS = {
    'smsc_ru': {
        'login': 'login', # require
        'password': 'password', # require, may be md5 hash of you password
        'sender': '', # not require. default empty
    },


}
```

`python manage.py syncdb`
or
`python manage.py migrate anysms`
if you use South


```python
from anysms.handlers import get_handler

h = get_handler('smsc_ru)
h.send('phone', 'message')
```
