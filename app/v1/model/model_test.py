# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-18 21:29 
# file: model_test.py
# ide: PyCharm
from app.app import db


class Test(db.Model):
    '''
    测试model
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
