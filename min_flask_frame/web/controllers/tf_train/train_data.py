# -*- coding: utf-8 -*-
from web.controllers.tf_train import route_tfTrain
from flask import request, jsonify, g
import json, decimal
from application import app,db
from flask import Blueprint,request,jsonify,make_response,redirect,g
from common.libs.UrlManager import UrlManager
from common.libs.Helper import ops_render
from common.models.tf_train.train_info import TrainInfo
@route_tfTrain.route("/train_data")
def train_data():
    return "this tf_train_data clude {" \
           "1.train_info" \
           "2.updata_train_info" \
           "}"

@route_tfTrain.route("/train_data/train_info", methods = ["GET"])
def get_info():
    resp = {'code':200, 'msg':'操作成功', 'data': {}}
    req = request.values
    dataset_name = req['dataset_name'] if 'dataset_name' in req else None

    data_info_dict = []
    if dataset_name:
        data_info = TrainInfo.query.filter(TrainInfo.dataset_name == dataset_name).all()
        if not data_info:
            resp['msg'] = '没有这个数据'
            return resp
    else:
        data_info = TrainInfo.query.filter().all()
    for item in data_info:
        data_info_dict.append({
            'id':item.id,
            'method':item.method,
            'data_name':item.dataset_name,
            'accuracy':item.accuracy
        })

    resp['data'] = data_info_dict
    return resp

