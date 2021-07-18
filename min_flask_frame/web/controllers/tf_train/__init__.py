from flask import Blueprint

route_tfTrain = Blueprint('tf_train',__name__)
from web.controllers.tf_train.train_data import *

@route_tfTrain.route("/")
def index():
    return "this is tf_train_data"