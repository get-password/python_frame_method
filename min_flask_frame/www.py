# -*- coding: utf-8 -*-
from application import app
'''
蓝图功能
'''
from web.controllers.index import route_index
from web.controllers.tf_train import route_tfTrain
'''
注册URL
'''
app.register_blueprint( route_index,url_prefix = "/" )
app.register_blueprint(route_tfTrain,url_prefix = "/tf")
