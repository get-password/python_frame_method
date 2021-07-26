# -*- coding: utf-8 -*-
SERVER_PORT = 8889
DEBUG = True
SQLALCHEMY_ECHO = True
RELEASE_VERSION = '20210726'


APP = {
    'domain':'https://vigigo.work',
}

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

# JSON_AS_ASCII = False
# AUTH_COOKIE_NAME = "vigigo"