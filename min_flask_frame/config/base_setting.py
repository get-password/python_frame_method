# -*- coding: utf-8 -*-
SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False
RELEASE_VERSION = '20210726'


APP = {
    'domain':'http://vigigo.work',
}

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

# JSON_AS_ASCII = False
# AUTH_COOKIE_NAME = "vigigo"