# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db

class TrainInfo(db.Model):
    __tablename__ = 'train_info'

    id = db.Column(db.BigInteger, primary_key=True)
    dataset_name = db.Column(db.String(40), nullable=False, server_default=db.FetchedValue())
    method = db.Column(db.String(40), nullable=False, server_default=db.FetchedValue())
    accuracy = db.Column(db.Float(20))
    loss = db.Column(db.Float(20), nullable=False)
    illustrate = db.Column(db.Text)
    state = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    creat_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
