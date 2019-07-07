# -*- coding: utf-8 -*-
from flask import Flask
from app.v1 import *


def register_blueprint(app):
    '''
    注册蓝图
    :return:
    '''
    from app.v1.test import test_blueprint
    app.register_blueprint(test_blueprint)


def create_app():
    '''
    创建核心对象
    :return:
    '''
    app = Flask(__name__)
    # 注册蓝图
    register_blueprint(app)
    return app


app = create_app()
