# -*- coding: utf-8 -*-
from flask import Blueprint

route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
def index():
    return "This is the test web," \
           "if you see this web," \
           "welcome!"

@route_index.route("/test")
def test():
    return "这是一个除了首页的页面"