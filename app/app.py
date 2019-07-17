# -*- coding: utf-8 -*-
from flasgger import Swagger
from flask import Flask


# from app.v1 import *


def register_blueprint(app):
    '''
    注册蓝图
    :return:
    '''
    from app.v1.test import test_blueprint
    app.register_blueprint(test_blueprint)


def register_swagger(app):
    '''
    注册swagger
    :param app:
    :return:
    '''
    import config.config_swagger as config_swagger
    app.config.from_object(config_swagger)
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = config_swagger.SWAGGER_TITLE  # 配置大标题
    swagger_config['description'] = config_swagger.SWAGGER_DESC  # 配置公共描述内容
    swagger_config['host'] = config_swagger.SWAGGER_HOST  # 请求域名
    Swagger(app, config=swagger_config)


def register_common(app):
    '''
    注册common config
    :param app:
    :return:
    '''
    import config.config_common as config_common
    app.config.from_object(config_common)


def create_app():
    '''
    创建核心对象
    :return:
    '''
    app = Flask(__name__)
    # 注册蓝图
    register_blueprint(app)
    # 注册swagger
    register_swagger(app)
    return app


app = create_app()
